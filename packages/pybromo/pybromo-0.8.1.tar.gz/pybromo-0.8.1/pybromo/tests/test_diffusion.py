"""
Module containing automated unit tests for PyBroMo.

Running the tests requires `py.test`.
"""

import pytest
import numpy as np
import json

import pybromo as pbm


_SEED = 2345654342


# - GLOBAL SIMULATION PARAMETERS - - - - - - - - - - - - - - - - - - - - - - -

# Diffusion parameters
t_step = 0.5e-6   # (seconds) diffusion simulation time step
t_max = 1         # (seconds) time duration of the diffusion simulation

# Diffusion coefficients
Du = 12.0            # um^2 / s
D1 = Du*(1e-6)**2    # m^2 / s
D2 = D1/2

# Simulation box
box = pbm.Box(x1=-4.e-6, x2=4.e-6, y1=-4.e-6, y2=4.e-6, z1=-6e-6, z2=6e-6)

# Particles populations
particles_specs = dict(
    # Parameters needed for the diffusion simulation
    num_particles=(1, 3),   # number of particles in each population
    D=(D1, D2),             # (m^2 / s) diffusion coefficiens per population
    box=box,                # simulation box

    # Photo-physics parameters (needed only for timestamps simulation)
    E_values=(0.75, 0.25),     # FRET efficiencies for each population
    em_rates=(200e3, 300e3),   # Peak D+A emission rates (cps) per population

    # Backgroung rates (needed for timestamps simulation)
    bg_rate_d=1500,           # Poisson background rate (cps) Donor channel
    bg_rate_a=800,            # Poisson background rate (cps) Acceptor channel
    )


def randomstate_equal(rs1, rs2):
    if isinstance(rs1, np.random.RandomState):
        rs1 = rs1.get_state()
    assert isinstance(rs1, tuple)
    if isinstance(rs2, np.random.RandomState):
        rs2 = rs2.get_state()
    assert isinstance(rs1, tuple)
    assert len(rs1) == len(rs2)
    equal = True
    for x1, x2 in zip(rs1, rs2):
        test = x1 == x2
        if hasattr(test, '__array__'):
            test = test.all()
        equal &= test
    return equal


def create_diffusion_sim(psf=pbm.NumericPSF()):
    rs = np.random.RandomState(_SEED)
    specs = {k: v for k, v in particles_specs.items()
             if k in ['num_particles', 'D', 'box']}
    P = pbm.Particles.from_specs(**specs, rs=rs)

    S = pbm.ParticlesSimulation(t_step=t_step, t_max=t_max,
                                particles=P, box=box, psf=psf)
    S.simulate_diffusion(save_pos=True, total_emission=False, radial=False,
                         rs=rs)
    S.store.close()
    return S.hash()[:6]


def test_Box():
    box = pbm.Box(0, 1, 0, 1, 0, 2)
    assert (box.b == np.array([[0, 1], [0, 1], [0, 2]])).all()
    assert box.volume == 2
    assert box.volume_L == 2000
    box.__repr__()  # smoke test
    box_dict = box.to_dict()
    box2 = pbm.Box(**box_dict)
    assert (box.b == box2.b).all()
    box_json = box.to_json()
    box3 = pbm.Box(**json.loads(box_json))
    assert (box.b == box3.b).all()


def test_Particle():
    a = pbm.diffusion.Particle(D=0.1, x0=0, y0=0, z0=0)
    a_dict = a.to_dict()
    b = pbm.diffusion.Particle(**a_dict)
    assert a.D == b.D and a.x0 == b.x0 and a.y0 == b.y0 and a.z0 == b.z0


def test_Particles():
    rs = np.random.RandomState(_SEED)
    P = pbm.Particles(num_particles=20, D=D1, box=box, rs=rs)
    P.add(num_particles=15, D=D2)
    assert P.particles_counts == [20, 15]
    assert P.num_populations == 2
    assert P.diffusion_coeff_counts == [(D1, 20), (D2, 15)]
    with pytest.raises(ValueError):
        P.add(num_particles=1, D=D1)
    x1 = P.num_particles_to_slices((7, 8))
    x2 = [slice(0, 7, None), slice(7, 7+8, None)]
    for s1, s2 in zip(x1, x2):
        assert s1 == s2

    Di, counts = zip(*P.diffusion_coeff_counts)
    rs2 = np.random.RandomState()
    rs2.set_state(P.init_random_state)
    P2_list = pbm.Particles._generate(num_particles=counts[0], D=Di[0],
                                      box=P.box, rs=rs2)
    P2_list += pbm.Particles._generate(num_particles=counts[1], D=Di[1],
                                       box=P.box, rs=rs2)
    assert P.to_list() == P2_list

    # Test Particles random states
    assert randomstate_equal(P.rs, rs.get_state())
    assert randomstate_equal(P.init_random_state, np.random.RandomState(_SEED))
    assert not randomstate_equal(P.init_random_state, P.rs)

    # Test JSON serialization
    P_json = P.to_json()
    P3 = pbm.Particles.from_json(P_json)
    assert P.to_list() == P3.to_list()

    # Test alternative constructor
    rs = np.random.RandomState(_SEED)
    P4 = pbm.Particles.from_specs(
        num_particles=(20, 15), D=(D1, D2), box=box, rs=rs)
    assert P4.to_list() == P2_list


def test_diffusion_sim_random_state():
    for psf in (pbm.NumericPSF(), pbm.GaussianPSF()):
        # Initialize the random state
        rs = np.random.RandomState(_SEED)

        # Particles definition
        P = pbm.Particles.from_specs(
            num_particles=(5, 7), D=(D1, D2), box=box, rs=rs)

        # Time duration of the simulation (seconds)
        t_max = 0.01

        # Particle simulation definition
        S = pbm.ParticlesSimulation(t_step=t_step, t_max=t_max,
                                    particles=P, box=box, psf=psf)

        rs_prediffusion = rs.get_state()
        S.simulate_diffusion(total_emission=False, save_pos=True, verbose=True,
                             rs=rs, chunksize=2**13, chunkslice='times')
        rs_postdiffusion = rs.get_state()

        # Test diffusion random states
        saved_rs = S.traj_group._v_attrs['init_random_state']
        assert randomstate_equal(saved_rs, rs_prediffusion)
        saved_rs = S.traj_group._v_attrs['last_random_state']
        assert randomstate_equal(saved_rs, rs_postdiffusion)
        S.store.close()


def _test_diffusion_sim_core(psf):
    # Initialize the random state
    rs = np.random.RandomState(_SEED)
    P = pbm.Particles(num_particles=100, D=D1, box=box, rs=rs)
    t_max = 0.001
    time_size = t_max / t_step
    assert t_max < 1e4
    S = pbm.ParticlesSimulation(t_step=t_step, t_max=t_max,
                                particles=P, box=box, psf=psf)

    start_pos = [p.r0 for p in S.particles]
    start_pos = np.vstack(start_pos).reshape(S.num_particles, 3, 1)

    for wrap_func in [pbm.diffusion.wrap_mirror, pbm.diffusion.wrap_periodic]:
        for total_emission in [True, False]:
            sim = S._sim_trajectories(time_size, start_pos, rs=rs,
                                    total_emission=total_emission,
                                    save_pos=True, wrap_func=wrap_func)

    POS, em = sim
    POS = np.concatenate(POS, axis=0)
    # x, y, z = POS[:, :, 0], POS[:, :, 1], POS[:, :, 2]
    # r_squared = x**2 + y**2 + z**2

    DR = np.diff(POS, axis=2)
    dx, dy, dz = DR[:, :, 0], DR[:, :, 1], DR[:, :, 2]
    dr_squared = dx**2 + dy**2 + dz**2

    D_fitted = dr_squared.mean() / (6 * t_max)  # Fitted diffusion coefficient
    assert np.abs(D1 - D_fitted) < 0.01


def test_diffusion_sim_core_npsf():
    _test_diffusion_sim_core(pbm.NumericPSF())


def test_diffusion_sim_core_gpsf():
    _test_diffusion_sim_core(pbm.GaussianPSF())


def test_simulate_timestamps():
    hash_ = create_diffusion_sim()
    S = pbm.ParticlesSimulation.from_datafile(hash_, mode='w')

    rs = np.random.RandomState(_SEED)
    kw = dict(max_rates=(400e3,), populations=(slice(0, 35),), bg_rate=1000,
              rs=rs, save_pos=True)
    S.simulate_timestamps_mix(**kw)

    # The following two cases should not throw an error
    kw.update(overwrite=True, skip_existing=True,
              rs=np.random.RandomState(_SEED))
    S.simulate_timestamps_mix(**kw)
    kw.update(overwrite=True, skip_existing=False,
              rs=np.random.RandomState(_SEED))
    S.simulate_timestamps_mix(**kw)

    # This should still pass
    kw.update(overwrite=False, skip_existing=True,
              rs=np.random.RandomState(_SEED))
    S.simulate_timestamps_mix(**kw)

    # This should throw an ExistingArrayError
    kw.update(overwrite=False, skip_existing=False,
              rs=np.random.RandomState(_SEED))
    with pytest.raises(pbm.storage.ExistingArrayError):
        S.simulate_timestamps_mix(**kw)

    # But with a different initial random state should succeed
    kw.pop('rs')
    S.simulate_timestamps_mix(**kw)
    S.store.close()


def test_TimestampSimulation():
    for psf in (pbm.GaussianPSF(), pbm.NumericPSF()):
        hash_ = create_diffusion_sim(psf)
        S = pbm.ParticlesSimulation.from_datafile(hash_, mode='a')

        params = dict(
            em_rates = (400e3,),    # Peak emission rates (cps) for each population (D+A)
            E_values = (0.75,),     # FRET efficiency for each population
            num_particles = (1,),   # Number of particles in each population
            bg_rate_d = 1400,       # Poisson background rate (cps) Donor channel
            bg_rate_a = 800,        # Poisson background rate (cps) Acceptor channel
            )

        mix_sim = pbm.TimestampSimulation(S, **params)
        mix_sim.summarize()

        rs = np.random.RandomState(_SEED)
        mix_sim.run(rs=rs, overwrite=True)
        mix_sim.save_photon_hdf5()
