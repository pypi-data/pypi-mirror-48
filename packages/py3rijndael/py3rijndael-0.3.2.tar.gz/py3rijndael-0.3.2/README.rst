py3rijndael
===========

.. image:: https://travis-ci.org/meyt/py3rijndael.svg?branch=master
    :target: https://travis-ci.org/meyt/py3rijndael

.. image:: https://coveralls.io/repos/github/meyt/py3rijndael/badge.svg?branch=master
    :target: https://coveralls.io/github/meyt/py3rijndael?branch=master

.. image:: https://img.shields.io/pypi/pyversions/py3rijndael.svg
    :target: https://pypi.python.org/pypi/py3rijndael

Rijndael algorithm library for Python3.

Rijndael is the key algorithm of `AES <https://en.wikipedia.org/wiki/Advanced_Encryption_Standard>`_,
and there is some of implementations already exist:

- `pycrypto <https://github.com/dlitz/pycrypto>`_: Very old and not written in python.
- `pycryptodome <https://github.com/Legrandin/pycryptodome>`_: In road of ``pycrypto`` but alive.
- `python-cryptoplus <https://github.com/doegox/python-cryptoplus>`_:
  Tested and works fine. but, not in Python 3, also depend on ``pycrypto``.
- `RijndaelPbkdf <https://github.com/dsoprea/RijndaelPbkdf>`_:
  Tested and works fine. but, old PyPi release and not active (i have no time to wait for maintainer).
- https://gist.github.com/jeetsukumaran/1291836 : The gist i borrowed initial source.

Installation
------------

.. code:: bash

    pip install py3rijndael


Usage
-----

Follow the tests.
