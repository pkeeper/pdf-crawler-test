# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    # Main API views
    url(
        regex="^ProcessPDF/$",
        view=views.pdf_upload,
        name="pdf_upload",
    ),
    url(
        regex="^ListDocuments/$",
        view=views.ListDocuments.as_view(),
        name="List_Documents",
    ),
    url(
        regex="^ListDocument_URLs/$",
        view=views.ListDocumentURLs.as_view(),
        name="List_Document_URLs",
    ),
    url(
        regex="^ListURLs/$",
        view=views.ListURLs.as_view(),
        name="List_URLs",
    ),

    # Models management Views
    url(
        regex="^CrawledURL/~create/$",
        view=views.CrawledURLCreateView.as_view(),
        name='CrawledURL_create',
    ),
    url(
        regex="^CrawledURL/(?P<pk>\d+)/~delete/$",
        view=views.CrawledURLDeleteView.as_view(),
        name='CrawledURL_delete',
    ),
    url(
        regex="^CrawledURL/(?P<pk>\d+)/$",
        view=views.CrawledURLDetailView.as_view(),
        name='CrawledURL_detail',
    ),
    url(
        regex="^CrawledURL/(?P<pk>\d+)/~update/$",
        view=views.CrawledURLUpdateView.as_view(),
        name='CrawledURL_update',
    ),
    url(
        regex="^CrawledURL/$",
        view=views.CrawledURLListView.as_view(),
        name='CrawledURL_list',
    ),
    url(
        regex="^Document/~create/$",
        view=views.DocumentCreateView.as_view(),
        name='Document_create',
    ),
    url(
        regex="^Document/(?P<pk>\d+)/~delete/$",
        view=views.DocumentDeleteView.as_view(),
        name='Document_delete',
    ),
    url(
        regex="^Document/(?P<pk>\d+)/$",
        view=views.DocumentDetailView.as_view(),
        name='Document_detail',
    ),
    url(
        regex="^Document/(?P<pk>\d+)/~update/$",
        view=views.DocumentUpdateView.as_view(),
        name='Document_update',
    ),
    url(
        regex="^Document/$",
        view=views.DocumentListView.as_view(),
        name='Document_list',
    ),
    ]
