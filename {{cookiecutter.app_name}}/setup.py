from __future__ import print_function
from setuptools import setup, find_packages
from codecs import open
from os import path
import versioneer

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]


setup(
    name='{{cookiecutter.app_name}}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='{{cookiecutter.project_short_description}}',
    long_description=long_description,
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    download_url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}/tarball/' + __version__,
    license="http://www.apache.org/licenses/LICENSE-2.0.html",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='{{cookiecutter.full_name}}',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='{{cookiecutter.email}}'
)
