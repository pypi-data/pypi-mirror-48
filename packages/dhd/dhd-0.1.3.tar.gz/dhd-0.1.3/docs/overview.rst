========
Overview
========

Graph theory and evolutionary algorithm applied to city district heating network
design.

Motivation
----------

This project belongs to a series of numerical tools developed by the CREM
(https://www.crem.ch/) in the perspective of a better energy distribution and
consumption at the city scale.

Description
-----------

The design of a district heating network is closely related to the problem of
finding the Terminal Steiner Tree (TST) of a graph. Indeed for a given connected
graph and a given subset of nodes, called terminals, the TST is the network of
smallest weight connecting all terminals only once. This is the exact structure
needed for a district heating network connecting heat sinks (buildings) to a
heating source via a streets network.

This package implement a systematic way of finding the best possible network
within a given amount of numerical computation. Indeed the TST problem being
NP complete, an heuristic evolutive algorithm is used.

The heating load of the buildings is then distributed throughout all the
pipelines belonging to the district heating network.

Additional tools are available to download city geometries from the Open Street
Map (OSM) dataset, modify their content, reshape their structure or visualize
them as well as for obtaining information on the network characteristics.

Package structure
-----------------

The package is organized in modules as represented on the figure below. The
information on the city geometries and the district heating network is stored
in dataframes (*streets, sinks, sources, terminals, vertices, tst, pipelines,
...*) which evolve along with the design process.

.. figure::  https://gitlab.com/crem-repository/dhd/raw/master/docs/images/structure.png
   :align:   center

* **Network Design**:
  This is the core of the package. It takes the streets, sinks and source(s)
  as input and returns the district heating network.

  - The first module, *dhd.connect*, connects the terminals (sinks and
    source(s)) to the streets and store the updated network in the dataframe
    *vertices*. The multiple possible connections of each terminal are stored
    in the dataframe *terminals*.
  - The second module, *dhd.evolve*, implements the evolutive algorithm
    which seeks the best connection network and store it into the data frame
    *tst*.
  - The last module, *dhd.load*, spreads the sinks heating loads throughout
    the heating network and merge neighbour pipes of equal load into single
    pipelines, which are stored in the dataframe *pipelines*.

* **Data Generation**:
  This set allows to download any city geometries from the OSM dataset and to
  modify some of its data.

  - The module *dhd.city* defines a class associated to any given city. It
    automatically loads the geometries of its streets and buildings.
    Additional information such as the source location or the presence of
    natural barriers may be provided. All this information is organized into
    dataframes.
  - The module *dhd.modify* allows to easily select and modify rows and
    columns of the previously defined dataframes. Note that despite its being
    in the same set as *dhd.city* it may naturally be applied to dataframes of
    different origins.

* **Graphical Interface**
  The module *dhd.plot* is used to define a background interface displaying
  the provided streets, buildings, source(s) and natural barrier(s). The
  different geometries constructed along the design process can be plotted
  over the background.

* **Network Properties**
  The module *dhd.features* computes and displays properties of the designed
  network.
