This is a simple library for reading and writing .tps files as created and used by the tpsDig landmarking tool
created by F. James Rohlf.  https://life.bio.sunysb.edu/morph/

Installation
============
Installation is managed via poetry. https://pypi.org/project/poetry/

To install, first install poetry.
*Note for conda users*
In order to use a conda environment with poetry, you must first configure poetry to use your conda environment and
not create a new virtualenv environment. Example::

    poetry config settings.virtualenvs.path $CONDA_ENV_PATH
    poetry config settings.virtualenvs.create 0

Then run::

  poetry install
  poetry build
  cd dist
  pip install *.whl

