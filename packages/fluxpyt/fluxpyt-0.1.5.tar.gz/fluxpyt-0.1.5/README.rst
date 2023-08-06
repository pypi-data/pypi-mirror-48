fluxpyt
========

This package is developed to perform stationary 13C metabolic flux analysis 
calculations for estimation of intracellular flux distribution.
FluxPyt is written in python3. The anaconda package list is provided in 
the requirements.txt file.

The package was developed as a part of PhD work of Desai Trunil Shamrao at:

Systems Biology for Biofuels Group
Group Leader, Dr. Shireesh Srivastava
International Centre for Genetic Engineering and Biotechnology (ICGEB),
Aruna Asaf Ali Marg,
New Delhi.


Acknowledgements
================
The PhD fellowship of Trunil is funded by the Council for Scientific 
and Industrial Research (CSIR).
The project is funded by Department of Biotechnology (DBT)

The author specially thanks Ahmad for being there to discuss issues and to 
help get rid of few bugs.



Installation ( for Windows):
============================
These directions are written for Windows users who are not familiar with Python programming.

Download and install Anaconda distribution (version 3.4.4.0 was used in this tutorial).

Open an Anaconda command prompt.
Click on Windows start button.
Type 'anaconda'. A link to open Anaconda command promt will be shown.

Type following commands to create new environment in Anaconda for running fluxpyt:

	conda create -n fluxpyt_env python=3.6.1 numpy=1.12.1 scipy=0.19.0 sympy=1.0

	activate fluxpyt_env

	conda install -c conda-forge lmfit

	conda install -c sjpfenninger glpk

	conda install csvkit=0.9.1

	conda install matplotlib=2.0.2

	conda install pandas=0.20.1

	conda install spyder

	pip install fluxpyt



=========
Changelog
=========
Version 0.1.4
=============
-Cleared code to largely follow PEP 8 guidelines.


Version 0.1.5
=============
-Lower bounds and upper bounds of each reaction can be assigned by user. Note: User defined bounds will affect the final solution only if they affect the bounds of free fluxes.
-Initial values of free flux parameters selected ome by one by performing flux variability for each free flux taking into account the previously selected value for other free fluxes.

Version 0.1.4
=============
-Minor changes

Version 0.1.3
=============
-Changed installation directions in README.rst

Version 0.1.2
=============
-Changed installation directions in README.rst

Version 0.1.1
==============
-Project setup created by Pyscaffold.

-Generated documentation using Sphinx

Version 0.1
============
-Initial release





Note
====

This project has been set up using PyScaffold 2.5.8. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
