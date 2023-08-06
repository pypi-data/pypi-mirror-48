from setuptools import setup
import versioneer

project_name = 'pybromo'

# Metadata
long_description = """
PyBroMo
==========

A brownian motion and timestamps/lifetimes simulator for freely diffusing
fluorescent particles (or dyes) under confocal excitation. It can be used to
accurately simulate confocal single-molecule FRET experiments with or
without lifetime information.

"""

setup(name = project_name,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author = 'Antonino Ingargiola',
      author_email = 'tritemio@gmail.com',
      url = 'http://opensmfs.github.io/PyBroMo/',
      download_url = 'https://github.com/OpenSMFS/PyBroMo',
      install_requires = ['numpy', 'setuptools', 'tables', 'matplotlib',
                          'phconvert'],
      license = 'GPLv2',
      description = ('Simulator for confocal single-molecule fluorescence '
                     'experiments.'),
      long_description = long_description,
      platforms = ('Windows', 'Linux', 'Mac OS X'),
      classifiers=['Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Scientific/Engineering',
                   ],
      packages = ['pybromo', 'pybromo.utils', 'pybromo.tests'],
      package_data = {'pybromo': ['psf_data/*']},
      keywords = ('single-molecule FRET smFRET biophysics confocal '
                  'freely-diffusing brownian-motion simulator'),
      )
