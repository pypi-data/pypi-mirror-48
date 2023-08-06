============
Installation
============

Assuming you have `Python 3.X <https://www.python.org/downloads/>`_ installed,
you can simply install DHD with pip:

.. code-block:: bash

  $ pip install dhd

If you prefer to install it from source (git is required) run the following
commands:

.. code-block:: bash

  $ git clone https://gitlab.com/crem-repository/dhd.git
  $ pip install -r requirements.txt
  $ pip install .

We recommend to use a virtual environment for the installation.
Also jupyter notebooks (`Jupyter Notebook <http://jupyter.org/>`_) are necessary
to run the learning examples and are practical when using the package.

The spatial indexing in Python requires the ctypes Python wrapper
`Rtree <http://toblerity.org/rtree/>`_. Please follow the installation instructions
on the previous link.
