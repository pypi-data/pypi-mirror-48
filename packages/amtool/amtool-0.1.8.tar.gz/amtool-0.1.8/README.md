# Artifact Management Tool

[![PyPI version](https://img.shields.io/pypi/v/amtool.svg)](https://pypi.python.org/pypi/amtool/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/amtool.svg)](https://pypi.python.org/pypi/amtool/)
[![Travis](https://api.travis-ci.org/bellockk/amtool.svg?branch=master)](https://travis-ci.org/bellockk/amtool/)
[![CodeCov](https://codecov.io/gh/bellockk/amtool/branch/master/graph/badge.svg)](https://codecov.io/gh/bellockk/amtool)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bellockk/amtool/master)
[![Documentation Status](https://readthedocs.org/projects/amtool/badge/?version=latest)](http://amtool.readthedocs.io/?badge=latest)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Statement of Purpose
--------------------

AMT is meant to be a generic means of storing and manipulating artifact data in a human readable text format ideal for colaborative work.

### What AMT is:
* An object oriented heirarchical data management tool.
* Designed to be used from the command line or user interface.
* Intended to manage human readable files captured in a version control system.
* Scriptable (Written in Python with extendable API)
* Embeddable (C++ api to follow)

### What AMT is not:
* Specialized for any task other than the storage and manipulation of artifacts.

### Intended Use Cases:
* Distributed Issue Tracking System
* Colaborative Requirements Management
* Use Case Documentation
* Object Models
* Software Lifecycle/Project Management Documentation Generation
* Simulation Input Files

### What problem does AMT try to solve.
The ability to colaboratively develop artifacts when a central server or database cannot be utilized.

#### Case Study: Distributed Issue Tracking
Examples of a use case for which there is no existing workable solution, is the requirement to use an issue tracking system for a project that will be worked by groups on multiple networks, sites, locations, and/or classification levels, where access to a central database or server cannot be maintained by all developers, all the time.  There are several excellent issue tracking systems out there, Bugzilla, Trac, Jira, but all of those solutions require access to a centralized server to interact with the issue database.  AMT provides a user definable solution to create, manage, and version control an issue database, in human readable format, within the repository the project is stored in.

### Command line tools
Command line tools are executed through subcommands of the amt command.

| Command    | Usage                                                              |
|:----------:|:-------------------------------------------------------------------|
| dump       | Dumps an ascii representation of the object tree.                  |
| cannonical | Enforces the canonical representation of the object tree.          |

### Example Python Usage
```python
import amt

# Load
artifacts = amt.load('/path/to/artifacts')

# Read
AMT_OAR_001 = artifacts['Requirements']['AMT-OAR-0001']

# Modify
artifacts['Requirements']['AMT-OAR-0002']['Description'] = 'Be Cool'

# Write
amt.save('/path/to/write/artifacts', artifacts)
```


## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
