.. image:: https://img.shields.io/badge/python-3-blue.svg
   :target: https://www.python.org/
   :alt: Python 3

.. image:: https://api.codeclimate.com/v1/badges/471b178f14d470337668/maintainability
   :target: https://codeclimate.com/github/edukorg/tsuru-py/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/471b178f14d470337668/test_coverage
   :target: https://codeclimate.com/github/edukorg/tsuru-py/test_coverage
   :alt: Test Coverage


================
Tsuru API Client
================

Python client for the `Tsuru <https://tsuru.io/>`_ API.

************
Installation
************

.. code-block:: bash

    pip install tsuru


*****
Setup
*****

The following environment variables must be set prior to using the lib.

``TSURU_URL``, with port (if necessary) and without trailing dash. Example: http://my-tsuru.domain.vpc:8080

``TSURU_USERNAME``

``TSURU_PASSWORD``


*****
Usage
*****

.. code-block:: python

    from tsuru import App

    for app in App.list()
        print(app.name)
