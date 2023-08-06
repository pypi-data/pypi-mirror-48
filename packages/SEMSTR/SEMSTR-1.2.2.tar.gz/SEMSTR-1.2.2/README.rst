Scheme Evaluation and Mapping for Structural Text Representation
================================================================

Collection of utilities for conversion and evaluation of semantic and
syntactic text representation schemes.

Requirements
~~~~~~~~~~~~

-  Python 3.6

Install
~~~~~~~

Create a Python virtual environment:

::

    virtualenv --python=/usr/bin/python3 venv
    . venv/bin/activate              # on bash
    source venv/bin/activate.csh     # on csh

Install the latest release:

::

    pip install semstr

Alternatively, install the latest code from GitHub (may be unstable):

::

    git clone https://github.com/danielhers/semstr
    cd semstr
    python setup.py install

Author
------

-  Daniel Hershcovich: danielh@cs.huji.ac.il

License
-------

This package is licensed under the GPLv3 or later license (see
```LICENSE.txt`` <LICENSE.txt>`__).

|Build Status (Travis CI)| |Build Status (AppVeyor)| |Build Status
(Docs)| |PyPI version|

.. |Build Status (Travis CI)| image:: https://travis-ci.org/danielhers/semstr.svg?branch=master
   :target: https://travis-ci.org/danielhers/semstr
.. |Build Status (AppVeyor)| image:: https://ci.appveyor.com/api/projects/status/github/danielhers/semstr?svg=true
   :target: https://ci.appveyor.com/project/danielh/semstr
.. |Build Status (Docs)| image:: https://readthedocs.org/projects/semstr/badge/?version=latest
   :target: http://semstr.readthedocs.io/en/latest/
.. |PyPI version| image:: https://badge.fury.io/py/SEMSTR.svg
   :target: https://badge.fury.io/py/SEMSTR
