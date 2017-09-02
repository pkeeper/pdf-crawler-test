from django.shortcuts import render
from django.http import HttpResponse
from ..pdftools import handle_pdf


def pdf_upload(request):
    if request.method == 'POST' and request.FILES:
        for filename, file in request.FILES.iteritems():
            handle_pdf(name=request.FILES[filename].name,
                       data=request.FILES[filename])
        return HttpResponse(status=200, content="OK")
    elif not request.FILES:
        pass
        #FIXME: Return right HTTP responce code
    return render(request, 'pdf_crawler_test/pdf_upload.html')
