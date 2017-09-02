=============================
PDF Crawler (test assignment)
=============================

.. image:: https://badge.fury.io/py/pdf-crawler-test.svg
    :target: https://badge.fury.io/py/pdf-crawler-test

.. image:: https://travis-ci.org/pkeeper/pdf-crawler-test.svg?branch=master
    :target: https://travis-ci.org/pkeeper/pdf-crawler-test

.. image:: https://codecov.io/gh/pkeeper/pdf-crawler-test/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pkeeper/pdf-crawler-test

Test assignment for CoMeet

Documentation
-------------

The full documentation is at https://pdf-crawler-test.readthedocs.io.

Quickstart
----------

Install PDF Crawler (test assignment)::

    pip install pdf-crawler-test

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pdf_crawler_test.apps.PdfCrawlerTestConfig',
        ...
    )

Add PDF Crawler (test assignment)'s URL patterns:

.. code-block:: python

    from pdf_crawler_test import urls as pdf_crawler_test_urls


    urlpatterns = [
        ...
        url(r'^', include(pdf_crawler_test_urls)),
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
