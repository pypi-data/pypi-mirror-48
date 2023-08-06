import os
import sys
from setuptools import setup, find_packages

install_requires = [
    'numpy>=1.10.0',
    'scipy>=0.18.0',
    'scikit-learn>=0.19.1',
    'pandas>=0.19.0,<0.24',
    'decorator>=4.3.0'
]

test_requires = [
    'nose',
    'nose2',
    'fcsparser',
    'tables',
    'h5py',
    'rpy2>=3.0',
    'coverage',
    'coveralls'
]

doc_requires = [
    'sphinx<=1.8.5',
    'sphinxcontrib-napoleon',
    'autodocsumm',
    'ipykernel',
    'nbsphinx',
]

if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >=3.5 required.")
elif sys.version_info[:2] < (3, 6):
    test_requires += ['matplotlib>=3.0,<3.1']
else:
    test_requires += ['matplotlib>=3.0']

version_py = os.path.join(os.path.dirname(
    __file__), 'scprep', 'version.py')
version = open(version_py).read().strip().split(
    '=')[-1].replace('"', '').strip()

readme = open('README.rst').read()

setup(name='scprep',
      version=version,
      description='scprep',
      author='Jay Stanley, Scott Gigante, and Daniel Burkhardt, Krishnaswamy Lab, Yale University',
      author_email='krishnaswamylab@gmail.com',
      packages=find_packages(),
      license='GNU General Public License Version 2',
      install_requires=install_requires,
      extras_require={'test': test_requires,
                      'doc': doc_requires},
      test_suite='nose2.collector.collector',
      long_description=readme,
      url='https://github.com/KrishnaswamyLab/scprep',
      download_url="https://github.com/KrishnaswamyLab/scprep/archive/v{}.tar.gz".format(
          version),
      keywords=['big-data',
                'computational-biology',
                ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Framework :: Jupyter',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
      ]
      )
