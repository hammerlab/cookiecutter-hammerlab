CookieCutter Pip-Project
========================

A cookiecutter template for python projects intended to be pip-installed

[cookiecutter](https://github.com/audreyr/cookiecutter)

Inspired by: [sloria](https://github.com/sloria/cookiecutter-flask.git)


Using CookieCutter for your project
-----------------------------------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/jburos/cookiecutter-hammerlab.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.


Publishing your project to pypi
-------------------------------

There are two ways to publish your project:

 * the manual way, outlined [here](http://www.willmcginnis.com/2015/11/12/create-a-pip-installable-python-package-in-2-minutes/)
 * and with pypi-publisher [ppp](https://github.com/wdm0006/pypi-publisher)
 
Goals
-----

The goal of this project is simply to take some of the boiler plate out of creating a new python project. It is intended
to stay pretty minimal, but contains best-practices in use by the Hammer Lab. 

These projects at a minimum will include:

 * Sphinx documentation
 * Installable via pip in pypi
 * Testing via Nose and Coverage
 * Code linting via pylint 
 * Travis CI configuration

Contributing
------------

The intent of this project is to stay fairly lean, but up to date with current best-practices in use by our lab.

License
-------

BSD licensed.
