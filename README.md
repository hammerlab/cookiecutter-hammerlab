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


Goals
-----

The goal of this project is simply to take some of the boiler plate out of creating a new Cohorts project. It is intended
to stay pretty minimal, but contains basic recommended structure of a Cohorts project. 

The components of the repo currently include:

 * `requirements.txt` file listing dependencies
 * `README.md` file with project description & data sources
 * Code linting via pylint 
 * `data` directory to contain source data & cached summaries
 * `analysis` directory to contain utility scripts & ipynbs

Contributing
------------

The intent of this project is to stay fairly lean, but up to date with current best-practices in use by our lab.

License
-------

BSD licensed.
