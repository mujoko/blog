# blog
Djanggo
Initial Set Up
The setup for this project is similar to past examples in this book:
make a new directory for our code called blog
install Django in a new virtual environment called .venv create a new Django project called django_project create a new app blog
perform a migration to set up the database
update django_project/settings.py

# Windows
$ cd onedrive\desktop\code
$ mkdir blog
$ cd blog
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $

# macOS
$ cd ~/desktop/code
$ mkdir blog
$ cd blog
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $

# Shell
(.venv) $ python -m pip install django~=5.0.0
(.venv) $ python -m pip install black
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py startapp blog
(.venv) $ python manage.py migrate


# django_project/settings.py
INSTALLED_APPS = [ "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "blog", # new
]


(.venv) $ python manage.py createsuperuser
Username (leave blank to use 'wsv'): wsv
Email:
Password:
Password (again):
Superuser created successfully.



# django_project/settings.py
TEMPLATES = [
    {
        ...
        "DIRS": [BASE_DIR / "templates"], # new
        ...
    },
]