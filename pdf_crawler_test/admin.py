from django.contrib import admin

from .models import CrawledURL,Document

admin.site.register(Document)
admin.site.register(CrawledURL)
