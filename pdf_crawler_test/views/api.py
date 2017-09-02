from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def handle_pdf(pdf):
    #(pdf.read())
    print ("Got a File!")

def pdf_upload(request):
    if request.method == 'POST' and request.FILES:
        for pdf in request.FILES.values():
            handle_pdf(pdf=pdf)
        return HttpResponse(status=200, content="OK")
    elif not request.FILES:
        pass
        #FIXME: Return right HTTP responce code
    return render(request, 'pdf_crawler_test/pdf_upload.html')
