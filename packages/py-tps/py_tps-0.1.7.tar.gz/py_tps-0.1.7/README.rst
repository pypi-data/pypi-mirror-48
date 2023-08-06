This is a simple library for reading and writing .tps files as created and used by the tpsDig landmarking tool
created by F. James Rohlf.  https://life.bio.sunysb.edu/morph/

Installation
============
The primary way to install is from pip::

    pip install py_tps

Installation from source is managed via poetry. https://pypi.org/project/poetry/
Source can be obtained from https://gitlab.com/ryan-feather/py_tps

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

Usage
=====
::

    from py_tps import TPSFile, TPSImage, TPSCurve, TPSPoints
    import numpy as np

    # construct and write
    # numpy is used for numeric data
    points = TPSPoints(np.asarray([[33,44],
                                   [44,45]]))
    curve = TPSCurve(points)
    image = TPSImage('T1.JPG', curves=[curve], id_number=0, comment="This is a test", scale=0.0045)
    tps_file = TPSFile([image]) # can have many images, but here we do just one
    tps_file.write_to_file('TestFile.TPS')

Creates a file with the contents::

    LM=0
    CURVES=1
    POINTS=2
    33 44
    44 45
    IMAGE=T1.JPG
    ID=0
    COMMENT=This is a test
    SCALE=0.0045


Now to read::

    tps_file_in =TPSFile.read_file('TestFile.TPS')
    # now can access images list, and so on.  Attributes have the same names as they do in the objects above.
    print(tps_file.images[0].image) # T1.JPG
    print(tps_file.images[0].curves[0].tps_points.points) # [[33,44],[44,45]]

Landmarks can be set instead of or with curves. If we instead do::

        image = TPSImage('T1.JPG', landmarks=points, id_number=0, comment="This is a test", scale=0.0045)

It creates the file with contents::

    LM=2
    33 44
    44 45
    IMAGE=T1.JPG
    ID=0
    COMMENT=This is a test
    SCALE=0.0045
