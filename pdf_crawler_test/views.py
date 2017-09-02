# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	CrawledURL,
	Document,
)


class CrawledURLCreateView(CreateView):

    model = CrawledURL


class CrawledURLDeleteView(DeleteView):

    model = CrawledURL


class CrawledURLDetailView(DetailView):

    model = CrawledURL


class CrawledURLUpdateView(UpdateView):

    model = CrawledURL


class CrawledURLListView(ListView):

    model = CrawledURL


class DocumentCreateView(CreateView):

    model = Document


class DocumentDeleteView(DeleteView):

    model = Document


class DocumentDetailView(DetailView):

    model = Document


class DocumentUpdateView(UpdateView):

    model = Document


class DocumentListView(ListView):

    model = Document

