=============================
exo_populator
=============================

.. image:: https://badge.fury.io/py/lib-exo-populator.svg
    :target: https://badge.fury.io/py/lib-exo-populator

.. image:: https://requires.io/github/exolever/lib-exo-populator/requirements.svg?branch=master
     :target: https://requires.io/github/exolever/lib-exo-populator/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://travis-ci.org/exolever/lib-exo-populator.svg?branch=master
    :target: https://travis-ci.org/exolever/lib-exo-populator

.. image:: https://codecov.io/gh/exolever//branch/master/graph/badge.svg
    :target: https://codecov.io/gh/exolever/lib-exo-populator

.. image:: https://sonarcloud.io/api/project_badges/measure?project=exolever_lib_exo_populator&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=exolever_lib_exo_populator

Generic populate models in django from YAML files

Documentation
-------------

The full documentation is at https://lib-exo-populator.readthedocs.io.

Quickstart
----------

Install exo_populator::

    pip install lib-exo-populator

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'populate.apps.PopulateConfig',
        ...
    )

Add exo_populator's URL patterns:

.. code-block:: python

    from populate import urls as populate_urls


    urlpatterns = [
        ...
        url(r'^', include(populate_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
