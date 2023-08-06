========
dhd.city
========

Module defining the class *City* which allows to load information from Open
Street Map (OSM) about the street network and the buildings geometries of a
given city.

Inputs
------

The user must provide the name of the considered city (*name*), for instance
'Vevey, Switzerland'. Heating sources and natural barriers (rivers,
railways,...) coordinates may as well be provided as lists of shapely
geometries.

Outputs
-------

All the city information is organized in dataframes. The streets network
(*streets*), the buildings to be connected (*sinks*), the heating sources
(*sources*) and the natural barriers (*barriers*) are respectively obtained
with the methods *get_streets()*, *select_sinks()*, *get_sources()* and
*get_barriers()*.

Class
-----

.. autoclass:: dhd.city.City
	:members:
	:private-members:
