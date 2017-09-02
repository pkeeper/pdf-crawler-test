# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from pdf_crawler_test.urls import urlpatterns as pdf_crawler_test_urls

urlpatterns = [
    url(r'^', include(pdf_crawler_test_urls, namespace='pdf_crawler_test')),
]
