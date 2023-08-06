
**Safe code refactoring for modern Python projects.**


.. image:: https://travis-ci.com/facebookincubator/Bowler.svg?branch=master
   :target: https://travis-ci.com/facebookincubator/Bowler
   :alt: build status


.. image:: https://img.shields.io/coveralls/github/facebookincubator/Bowler/master.svg
   :target: https://coveralls.io/github/facebookincubator/Bowler
   :alt: code coverage


.. image:: https://img.shields.io/pypi/v/bowler.svg
   :target: https://pypi.org/project/bowler
   :alt: version


.. image:: https://img.shields.io/badge/change-log-blue.svg
   :target: https://github.com/facebookincubator/bowler/blob/master/CHANGELOG.md
   :alt: changelog


.. image:: https://img.shields.io/pypi/l/bowler.svg
   :target: https://github.com/facebookincubator/bowler/blob/master/LICENSE
   :alt: license


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: code style


Overview
--------

Bowler is a refactoring tool for manipulating Python at the syntax tree level. It enables
safe, large scale code modifications while guaranteeing that the resulting code compiles
and runs. It provides both a simple command line interface and a fluent API in Python for
generating complex code modifications in code.

Bowler uses a "fluent" ``Query`` API to build refactoring scripts through a series
of selectors, filters, and modifiers.  Many simple modifications are already possible
using the existing API, but you can also provide custom selectors, filters, and
modifiers as needed to build more complex or custom refactorings.  See the
`Query Reference <https://pybowler.io/docs/api-query>`_ for more details.

Using the query API to rename a single function, and generate an interactive diff from
the results, would look something like this:

.. code-block:: python

   query = (
       Query(<paths to modify>)
       .select_function("old_name")
       .rename("new_name")
       .diff(interactive=True)
   )

For more details or documentation, check out https://pybowler.io

Installing Bowler
-----------------

Bowler supports modifications to code from any version of Python 2 or 3, but it
requires Python 3.6 or higher to run. Bowler can be easily installed using most common
Python packaging tools. We recommend installing the latest stable release from
`PyPI <https://pypi.org/p/bowler>`_ with ``pip``\ :

.. code-block:: bash

   pip install bowler

You can also install a development version from source by checking out the Git repo:

.. code-block:: bash

   git clone https://github.com/facebookincubator/bowler
   cd bowler
   python setup.py install

License
-------

Bowler is MIT licensed, as found in the ``LICENSE`` file.
