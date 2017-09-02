=====
Usage
=====

To use PDF Crawler (test assignment) in a project, add it to your `INSTALLED_APPS`:

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
