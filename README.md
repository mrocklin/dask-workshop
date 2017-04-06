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
within this directory.  They depend on the following libraries

    conda install -c conda-forge dask distributed jupyter bokeh feather-format python-graphviz matplotlib
    pip install pandas_datareader

Artificial data is automatically generated as part of the notebooks.
