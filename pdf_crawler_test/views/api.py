from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from .mixins import JSONResponseMixin
from ..models import Document, CrawledURL
from ..pdftools import handle_pdf


def pdf_upload(request):
    if request.method == 'POST':
        if request.FILES:
            try:
                for postfile in request.FILES.values():
                    handle_pdf(name=postfile.name,
                               data=postfile)
            except Exception as e:
                return HttpResponse(status=400, content=str(e))
            else:
                return HttpResponse(status=200, content="OK")
        else:
            return HttpResponse(status=400, content="No files attached")
    return render(request, 'pdf_crawler_test/pdf_upload.html')


class ListDocuments(JSONResponseMixin, BaseListView):
    model = Document


class ListDocumentURLs(JSONResponseMixin, BaseDetailView):
    model = Document

    def get_context_data(self, **kwargs):
        context = super(ListDocumentURLs, self).get_context_data(**kwargs)
        context[self.context_object_name] = context[self.context_object_name].urls_list
        return context


class ListURLs(JSONResponseMixin, BaseListView):
    model = CrawledURL
