============
How to use ?
============

Import the package modules:

.. code-block:: python

  from dhd import city, connect, evolve, load

Load the geometries of the city of Vevey in Switzerland:

.. code-block:: python

  vevey = city.City('Vevey, Switzerland', sources=Point(333795, 5147530))
  streets = vevey.get_streets()
  sinks = vevey.select_sinks(min_load=300)
  sources = vevey.get_sources()

Connect the selected buildings (sinks) and the source to the streets network:

.. code-block:: python

  vertices, terminals = connect.connect_terminals(streets, sinks, sources)

Run the evolutive algorithm to seek the best possible heating network within
five generations:

.. code-block:: python

  N = 5
  evolution = evolve.run_evolution(vertices, terminals, N)
  tst = evolve.get_best_terminal_steiner_tree(vertices, terminals, evolution)

Spread the buildings load over the district heating pipelines:

.. code-block:: python

  pipelines = load.load_the_pipelines(tst, terminals)

More detailed `examples
<https://gitlab.com/crem-repository/dhd/tree/master/notebooks>`_ are provided in
the GitLab repository.
