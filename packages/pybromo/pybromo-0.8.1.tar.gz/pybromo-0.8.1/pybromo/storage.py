#
# PyBroMo - A single molecule diffusion simulator in confocal geometry.
#
# Copyright (C) 2013-2015 Antonino Ingargiola tritemio@gmail.com
#

"""
This module implements functions to store simulation results to a file.
The module uses the HDF5 file format through the PyTables library.

File part of PyBroMo: a single molecule diffusion simulator.
Copyright (C) 2013-2014 Antonino Ingargiola tritemio@gmail.com
"""

from pathlib import Path
import time
import tables

from ._version import get_versions
__version__ = get_versions()['version']


# Compression filter used by default for arrays
default_compression = tables.Filters(complevel=5, complib='blosc')


def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


class ExistingArrayError(Exception):
    pass


class BaseStore(object):

    @staticmethod
    def calc_chunkshape(chunksize, shape, kind='bytes'):
        assert kind in ['times', 'bytes']
        if chunksize is None:
            return None

        divisor = 1
        if kind == 'bytes':
            for dimsize in shape[:-1]:
                divisor *= dimsize

        if len(shape) == 1:
            chunkshape = (chunksize / divisor,)
        elif len(shape) == 2:
            chunkshape = (shape[0], chunksize / divisor)
        elif len(shape) == 3:
            chunkshape = (shape[0], shape[1], chunksize / divisor)
        return chunkshape

    def __init__(self, datafile, path='./', nparams=dict(), attr_params=dict(),
                 mode='r'):
        """Return a new HDF5 file to store simulation results.

        The HDF5 file has two groups:
        '/parameters'
            containing all the simulation numeric-parameters

        If `mode='w'`, `datafile` will be overwritten (if exists).
        """
        if isinstance(datafile, Path):
            self.filepath = datafile
        else:
            if not Path(path).exists():
                raise ValueError('Path "%s" does not exists.' % path)
            self.filepath = Path(path, datafile)
        self.h5file = tables.open_file(str(self.filepath), mode=mode)
        self.filename = str(self.filepath)
        if mode == 'w':
            self.h5file.title = "PyBroMo simulation file"

            # Create the groups
            self.h5file.create_group('/', 'parameters', 'Simulation parameters')
            # Set the simulation parameters
            self.set_sim_params(nparams, attr_params)

    def close(self):
        self.h5file.close()

    def open(self):
        """Reopen a file after has been closed (uses the store filename)."""
        self.__init__(self.h5file.filename, mode='r')

    def set_sim_params(self, nparams, attr_params):
        """Store parameters in `params` in `h5file.root.parameters`.

        Argument:
            nparams (dict): a dict of parameters from
                `ParticlesSimulation().nparams`. The format is:

                keys:
                    used as parameter name
                values: (2-elements tuple)
                    first element is the parameter value
                    second element is a string used as "title" (description)

            attr_params (dict): dict items will be stored as attributes in
                '/parameters'
        """
        for name, value in nparams.items():
            val = value[0] if value[0] is not None else 'none'
            self.h5file.create_array('/parameters', name, obj=val,
                                     title=value[1])
        for name, value in attr_params.items():
            self.h5file.set_node_attr('/parameters', name, value)

    @property
    def numeric_params(self):
        """Return a dict containing all (key, values) stored in '/parameters'
        """
        nparams = dict()
        for par in self.h5file.root.parameters:
            nparams[par.name] = par.read()
        return nparams

    @property
    def numeric_params_meta(self):
        """Return a dict with all parameters and metadata in '/parameters'.

        This returns the same dict format as `ParticlesSimulation().nparams`.
        """
        nparams = dict()
        for par in self.h5file.root.parameters:
            nparams[par.name] = (par.read(), par.title)
        return nparams


class TrajectoryStore(BaseStore):
    """An on-disk HDF5 store for trajectories.
    """
    def __init__(self, datafile, path='./', nparams=dict(), attr_params=dict(),
                 mode='r'):
        """Return a new HDF5 file to store simulation results.

        The HDF5 file has two groups:
        '/parameters'
            containing all the simulation numeric-parameters

        '/trajectories'
            containing simulation trajectories (positions, emission traces)

        If `mode='w'`, `datafile` will be overwritten (if exists).
        """
        super().__init__(datafile, path=path, nparams=nparams,
                         attr_params=attr_params, mode=mode)
        if mode != 'r':
            # Create the groups
            self.h5file.create_group('/', 'trajectories',
                                     'Simulated trajectories')
            self.h5file.create_group('/', 'psf', 'PSFs used in the simulation')

    def add_trajectory(self, name, overwrite=False, shape=(0,), title='',
                       chunksize=2**19, chunkslice='bytes',
                       comp_filter=default_compression,
                       atom=tables.Float64Atom(), params=dict()):
        """Add an trajectory array in '/trajectories'.
        """
        group = self.h5file.root.trajectories
        if name in group:
            print("%s already exists ..." % name, end='')
            if overwrite:
                self.h5file.remove_node(group, name)
                print(" deleted.")
            else:
                print(" old returned.")
                return group.get_node(name)

        nparams = self.numeric_params
        num_t_steps = nparams['t_max'] / nparams['t_step']

        chunkshape = self.calc_chunkshape(chunksize, shape, kind=chunkslice)
        store_array = self.h5file.create_earray(
            group, name, atom=atom,
            shape = shape,
            chunkshape = chunkshape,
            expectedrows = num_t_steps,
            filters = comp_filter,
            title = title)

        # Set the array parameters/attributes
        for key, value in params.items():
            store_array.set_attr(key, value)
        store_array.set_attr('PyBroMo', __version__)
        store_array.set_attr('creation_time', current_time())
        return store_array

    def add_emission_tot(self, chunksize=2**19, chunkslice='bytes',
                         comp_filter=default_compression,
                         overwrite=False, params=dict()):
        """Add the `emission_tot` array in '/trajectories'.
        """
        kwargs = dict(overwrite=overwrite, params=params,
                      chunksize=chunksize, chunkslice=chunkslice,
                      comp_filter=comp_filter, atom=tables.Float32Atom(),
                      title='Summed emission trace of all the particles')
        return self.add_trajectory('emission_tot', **kwargs)

    def add_emission(self, chunksize=2**19, chunkslice='bytes',
                     comp_filter=default_compression,
                     overwrite=False, params=dict()):
        """Add the `emission` array in '/trajectories'.
        """
        nparams = self.numeric_params
        num_particles = nparams['np']

        return self.add_trajectory('emission', shape=(num_particles, 0),
                                   overwrite=overwrite, chunksize=chunksize,
                                   chunkslice=chunkslice,
                                   comp_filter=comp_filter,
                                   atom=tables.Float32Atom(),
                                   title='Emission trace of each particle',
                                   params=params)

    def add_position(self, radial=False, chunksize=2**19, chunkslice='bytes',
                     comp_filter=default_compression, overwrite=False,
                     params=dict()):
        """Add the `position` array in '/trajectories'.
        """
        nparams = self.numeric_params
        num_particles = nparams['np']

        name, ncoords, prefix = 'position', 3, 'X-Y-Z'
        if radial:
            name, ncoords, prefix = 'position_rz', 2, 'R-Z'
        title = '%s position trace of each particle' % prefix
        return self.add_trajectory(name, shape=(num_particles, ncoords, 0),
                                   overwrite=overwrite, chunksize=chunksize,
                                   chunkslice=chunkslice,
                                   comp_filter=comp_filter,
                                   atom=tables.Float32Atom(),
                                   title=title,
                                   params=params)


class TimestampStore(BaseStore):
    """An on-disk HDF5 store for timestamps.
    """
    def __init__(self, datafile, path='./', nparams=dict(), attr_params=dict(),
                 mode='r'):
        """Return a new HDF5 file to store simulation results.

        The HDF5 file has two groups:
        '/parameters'
            containing all the simulation numeric-parameters

        '/timestamps'
            containing simulated timestamps

        If `overwrite=True` (default) `datafile` is overwritten (if exists).
        """
        super().__init__(datafile, path=path, nparams=nparams,
                         attr_params=attr_params, mode=mode)
        if mode != 'r':
            if 'timestamps' not in self.h5file.root:
                self.h5file.create_group('/', 'timestamps',
                                         'Simulated timestamps')

    def add_timestamps(self, name, clk_p, max_rates, bg_rate,
                       num_particles, bg_particle, populations=None,
                       overwrite=False, chunksize=2**16,
                       comp_filter=default_compression, save_pos=False,
                       spatial_dims=None):
        if name in self.h5file.root.timestamps:
            if overwrite:
                self.h5file.remove_node('/timestamps', name=name)
                self.h5file.remove_node('/timestamps', name=name + '_par')
                try:
                    self.h5file.remove_node('/timestamps', name=name + '_pos')
                except tables.NoSuchNodeError:
                    pass
            else:
                msg = 'Timestamp array already exist (%s)' % name
                raise ExistingArrayError(msg)

        times_array = self.h5file.create_earray(
            '/timestamps', name, atom=tables.Int64Atom(),
            shape = (0,),
            chunkshape = (chunksize,),
            filters = comp_filter,
            title = 'Simulated photon timestamps')
        times_array.set_attr('clk_p', clk_p)
        times_array.set_attr('max_rates', max_rates)
        times_array.set_attr('bg_rate', bg_rate)
        times_array.set_attr('populations', populations)
        times_array.set_attr('PyBroMo', __version__)
        times_array.set_attr('creation_time', current_time())
        particles_array = self.h5file.create_earray(
            '/timestamps', name + '_par', atom=tables.UInt8Atom(),
            shape = (0,),
            chunkshape = (chunksize,),
            filters = comp_filter,
            title = 'Particle number for each timestamp')
        particles_array.set_attr('num_particles', num_particles)
        particles_array.set_attr('bg_particle', bg_particle)
        particles_array.set_attr('PyBroMo', __version__)
        particles_array.set_attr('creation_time', current_time())
        positions_array = None
        if save_pos:
            assert spatial_dims is not None, 'You need to pass `spatial_dims`.'
            positions_array = self.h5file.create_earray(
                '/timestamps', name + '_pos', atom=tables.Float32Atom(),
                shape=(0, spatial_dims),
                chunkshape=(chunksize, spatial_dims),
                filters=comp_filter,
                title='Particle position for each timestamp')
            positions_array.set_attr('PyBroMo', __version__)
            positions_array.set_attr('creation_time', current_time())
        return times_array, particles_array, positions_array


if __name__ == '__main__':
    d = {'D': (1.2e-11, 'Diffusion coefficient (m^2/s)'),
         'EID': (0, 'IPython engine ID (int)'),
         'ID': (0, 'Simulation ID (int)'),
         'np': (40, 'Number of simulated particles'),
         'pico_mol': (86.4864063019005, 'Particles concentration (pM)'),
         't_max': (0.1, 'Simulation total time (s)'),
         't_step': (5e-07, 'Simulation time-step (s)')}
    store = TrajectoryStore('h2.h5', d)

#    em_tot_array = add_em_tot_array(hf)
#    em_array = add_em_array(hf)
#
#    #%%timeit -n1 -r1
#    for i in range(0, int(n_rows/chunksize)):
#        em_tot_array.append(np.random.rand(chunksize))
#    em_tot_array.flush()
#
#
#    #%%timeit -n1 -r1
#    for i in xrange(0, int(n_rows/chunksize)):
#        em_array.append(np.random.rand(chunksize, num_particles))
#    em_array.flush()
#
