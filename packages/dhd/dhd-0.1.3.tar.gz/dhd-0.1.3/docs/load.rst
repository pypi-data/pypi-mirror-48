========
dhd.load
========

Module to reorganize the Terminal Steiner Tree (TST) computed with the module
*dhd.evolve* with a pipeline structure. A pipeline is defined as a merged series
of TST edges sharing the same load. The load of a pipeline is equal to the sum
of the heating loads of all the sinks it eventually leads to.

Functions to compute the pipelines diameters and nominal diameters are also
implemented.

Inputs
------

The user must provide the dataframe of the TST to load (*tst*) and the dataframe
of the terminals (*terminals*) with the loads. These two dataframes are computed
within the module *dhd.evolve*.

Outputs
-------

All the pipeline information is saved in a dataframe (*pipelines*) returned by
the function *dhd.load.load_the_pipelines*.

Functions
---------

.. automodule:: dhd.load
	:members:
	:private-members:
