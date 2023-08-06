==========
dhd.evolve
==========

List of functions to run the evolutive algorithm seeking for the best Terminal
Steiner Tree (TST) connecting all sinks and sources of the district heating
network.

Terminal Steiner Tree (TST)
---------------------------

The tree of minimal length connecting a set of terminals (subset of the graph
nodes) is called a Steiner Tree. Its exact computation is a NP complete problem,
so that an approximate algorithm is used. The worst possible ratio between the
weight of the approximated tree and the weight of the exact Steiner Tree is
*2-2/t*, where *t* is the number of terminals.

In the district heating design problem, the further constraint of single
terminal connection is imposed. The problem goes under the name of Terminal
Steiner Tree problem. No efficient algorithm exists, so that we use an evolutive
heuristic method.

Algorithm idea
--------------

For each terminal (*T_i*) there is a set of connections to the network. A
configuration of single connections is represented as a set of genes, called an
individual. The weight of an individual is the weight of its associated Steiner
Tree, which is a TST by construction.

.. figure::  https://gitlab.com/crem-repository/dhd/raw/master/docs/images/evolution.png
   :align:   center

The idea is to consider a population of *n* individual, to class them in
increasing order, to select the *n1*, respectively *n2*, lighter individuals to
form the elites, respectively the parents, populations. The elites are merely
mutated and reinjected in the population of the next generation. However the
parents are paired into *n-n1* couples which each procreate one child, by mixing
their genes. These *n-n1* children are then mutated and added to the next
generation population. This reproduction process is applied for *N* generations.

Inputs
------

The algorithm is designed to work on the dataframes *vertices* and *terminals*
constructed with the module *dhd.connect*. The user must also provide the number
of generation (*N*) and may specify the whole population size (*n*), the elite
population size (*n1*), the parent population size (*n2*) and the rate of gene
mutation (*mutation_rate*).

Outputs
-------

The whole evolution is saved in the dataframe *evolution* returned by the
function *dhd.evolve.run_evolution*. The TST dataframe associated to the best
configuration is returned by the function
*dhd.evolve.get_best_terminal_steiner_tree*.

Functions
---------

.. automodule:: dhd.evolve
	:members:
	:private-members:
