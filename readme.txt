I'm assuming that PDF's don't always have unique file name
and we don't have to check for unique content,
meaning that there may be documents with the same name or content
but with different ID's.
One could use hashes of the content if uniqueness check is needed.

To check app `cd` into example folder where example Django project located.
Setup project:

pip install -r requirements.txt
./manage.py migrate

Create superuser (if admin site is needed):
./manage.py createsuperuser

Run project
.manage.py runserver


