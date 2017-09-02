# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class CrawledURL(TimeStampedModel):
    url = models.URLField()

    @property
    def documents_count(self):
        return self.document_set.all().count()

    def to_dict(self):
        return {'url': self.url,
                'documents_count': self.documents_count}

    def __str__(self):
        return "CrawledURL[%s]" % self.url


@python_2_unicode_compatible
class Document(TimeStampedModel):
    name = models.CharField(max_length=255)
    urls = models.ManyToManyField(CrawledURL)

    @property
    def urls_count(self):
        return self.urls.all().count()

    def to_dict(self):
        return {
            'id': self.pk,
            'name': self.name,
            'urls_count': self.urls_count
        }

    def __str__(self):
        return "Document[%s]"% self.name



