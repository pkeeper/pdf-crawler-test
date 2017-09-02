I'm assuming that PDF's don't always have unique file name
and we don't have to check for unique content,
meaning that there may be documents with the same name or content
but with different ID's.
One could use hashes of the content if uniqueness check is needed.

URL is alive if it returns 2XX or 3XX code.

To check app `cd` into example folder where example Django project located.
Setup project:

pip install -r requirements.txt
./manage.py migrate

Create superuser (if admin site is needed):
./manage.py createsuperuser

Run project
.manage.py runserver


Usage

Add some PDFs:
http://127.0.0.1:8000/ProcessPDF/
There's a simple form to upload a file.
It can accept multiple files on POST (but no UI for that).
If file is not a valid PDF it will return 400 code with error message, else "OK".

List URLs that was detected in the PDF
http://127.0.0.1:8000/ListDocument_URLs/<id>/
Example:
http://127.0.0.1:8000/ListDocument_URLs/1/

List URLs
http://127.0.0.1:8000/ListURLs/

List Documents
http://127.0.0.1:8000/ListDocuments/
