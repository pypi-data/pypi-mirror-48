==================================================================
MAGINE : Mechanism of Action Generator involving Network Expansion
==================================================================

Installation
============

1. Install Anaconda

   Our recommended approach is to use Anaconda_, which is a
   distribution of Python containing most of the numeric and scientific
   software needed to get started. If you are a Mac or Linux user, have
   used Python before and are comfortable using ``pip`` to install
   software, you may want to skip this step and use your existing Python
   installation.

   Anaconda has a simple graphical installer which can be downloaded
   from https://www.anaconda.com/distribution/#download-section - select
   your operating system and download the **Python 3.7 version**. The
   default installer options are usually appropriate.

2. Open a terminal

   We will install most packages with conda::

      $ conda create -n magine_env python=3.7
      $ conda activate magine_env
      $ conda config --add channels conda-forge
      $ conda install jinja2 statsmodels networkx graphviz
      $ conda install -c marufr python-igraph

   **Windows users:** Please download and install igraph and pycairo
   using the wheel files provided by Christoph Gohlke, found at
   https://www.lfd.uci.edu/~gohlke/ . Download and install via pip.

3. Install MAGINE

   The installation is very straightforward with ``pip`` - type the following in a terminal::

      $ pip install magine

4. Start Python and MAGINE

   From the terminal or command prompt type ::

      $ jupyter notebook

   You will then be at the Python prompt. Type ``import magine`` to try
   loading magine. If no error messages appear and the next Python
   prompt appears, you have succeeded in installing magine!

Documentation
=============

The manual is available online at http://magine.readthedocs.io.

.. _Anaconda: https://www.anaconda.com/distribution/#download-section

