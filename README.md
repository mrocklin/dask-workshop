Dask Workshop
=============

These materials provide a brief hands-on introduction to the parallel computing
system, Dask.  They are intended to be delivered over a 90 minute session and
cover the following topics.

1.  Parallelize existing code with dask.delayed
2.  Set up the dask.distributed system on your local laptop
3.  Use Dask.dataframe on time series data

These topics are far from comprehensive, but have been chosen to give a flavor
for what can be done with Dask.

These materials are presented as Jupyter notebooks, which should be available
within this directory.  They depend on the following libraries:

    conda install -c conda-forge dask distributed jupyter bokeh feather-format python-graphviz matplotlib
    pip install pandas_datareader

Artificial data is automatically generated as part of the notebooks.

*Note: feather-format is not available in Python 2 on Windows.*

*Note: tornado 4.5 and bokeh 0.12.5 have known compatibility issues.*

You may want to create a new environment for this tutorial:

    conda create -n dask-workshop -c conda-forge python=3 dask distributed jupyter bokeh feather-format python-graphviz matplotlib tornado=4.4
    source activate dask-workshop
    pip install pandas_datareader
    jupyter notebook


After Finishing
---------------

This tutorial covered
[dask.dataframe](http://dask.pydata.org/en/latest/dataframe.html) and
[dask.delayed](http://dask.pydata.org/en/latest/delayed.html) for simple
tabular computations.  This is a common and important case, but is only one of
many applications for which Dask is used.  If you are interested in arrays,
machine learning, asynchronous computations, etc.  you may wish to peruse the
documentation further:

-  [Main Documentation](http://dask.pydata.org/en/latest/)
-  [Examples](http://dask.pydata.org/en/latest/examples-tutorials.html)
-  [Distributed scheduler](http://distributed.readthedocs.io/en/latest/) (also
   most of the asynchronous docs)

If you want to try Dask on a cluster on Amazon or Google hardware then you
might try one of the following projects:

-  [dask-ec2](http://distributed.readthedocs.io/en/latest/)
-  [dask-kubernetes](https://github.com/martindurant/dask-kubernetes)
