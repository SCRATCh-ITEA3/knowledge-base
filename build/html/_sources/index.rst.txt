.. practice2standards documentation master file, created by
   sphinx-quickstart on Thu Mar 25 23:03:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to practice2standards's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------

As part of the SCRATCh project: https://itea3.org/project/scratch.html research phase this tool
was deveopped to help navigate DCMS data (requirements/best practices).

https://iotsecuritymapping.uk/open-data-files-latest-v4/

There are two components in this project. The backend which reads the database from local file or 
webresouce and stores the data in a structure. 

The front end allows for making structures/filters and export.

..code-block::bash

python3 ui.py

Examples
--------

Simple startup front-end
++++++++++++++++++++++++

From the shell type:

.. code-block:: bash

   python3 ui.py

Open a browser and type:

http://localhost:5000

in the address-bar.

Backend usage
+++++++++++++

The follwing code will return all the properties of the guides beloning to
the organization `IEEE`. 

.. code-block:: python
   :linenos:

   gl = CodeOfPracticeReader()
   gl.setup()

   guides = gl.getGuides()

   processor = Processor(guides)

   list = processor.getOccurencesOfOrganisation(["IEEE"])

   for item in list:
      print (propsOf(item))

Multiple organizations can be selected:

.. code-block:: python

   list = processor.getOccurencesOfOrganisation(["IEEE", "W3C"])

etc, etc.


Class overview:
===============

.. automodule:: prototype
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
