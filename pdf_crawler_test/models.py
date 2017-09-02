# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class CrawledURL(TimeStampedModel):
    url = models.URLField()

    def __str__(self):
        return "CrawledURL[%s]" % self.url


@python_2_unicode_compatible
class Document(TimeStampedModel):
    name = models.CharField(max_length=255)
    urls = models.ManyToManyField(CrawledURL)

    def __str__(self):
        return "Document[%s]"% self.name



