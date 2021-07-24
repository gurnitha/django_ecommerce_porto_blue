## BUILDING DJANGO ECOMMERCE PORTO BLUE
https://github.com/gurnitha/django_ecommerce_porto_blue

### ----------
### 1. SETUP
### ----------


#### 1.1 Basic setup

        .Create venv and install django
        .Install drivers:
        ..pip install django-environ
        ..pip install psycopg2-binary==2.8.6
        ..pip install Pillow
        .pip install --upgrade pip

        new file:   .gitignore
        new file:   README.md

#### 1.2 Create Github repository and pust the project to Github

        https://github.com/gurnitha/django_ecommerce_porto_blue     

        modified:   README.md


### ---------------------------
### 2. DJANGO PROJECT AND APP
### ---------------------------


#### 2.1 Create django project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2.2 Create django app 'apps/main'

        (venv3932) λ mkdir apps\main
        (venv3932) λ python manage.py startapp main apps/main

        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/tests.py
        new file:   apps/main/views.py


#### 2.3 Register the main app to the project settings.py

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/settings.py 


### -------------
### 3. DATABASE
### -------------


#### 3.1 Create database using PostgreSQL

        hp=# CREATE DATABASE django_ecommerce_porto_blue;
        CREATE DATABASE
        hp=#


#### 3.2 Connect database with the project using django_environ

        (venv3932) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py


### --------------------------
### 4. ACTIVATE DJANGO ADMIN
### --------------------------


#### 4.1 Run migrations

        modified:   README.md


#### 4.2 Create superuser

        modified:   README.md


### -------------------------------------------
### 5. TEMPLATE, STATIC FILES, VIEWS AND URLS
### -------------------------------------------


#### 5.1 Activating template engine

        modified:   README.md
        modified:   config/settings.py


#### 5.2 Adding home template

        modified:   README.md
        new file:   templates/main/index.html


#### 5.3 Creating home views and urls

        modified:   README.md
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   config/urls.py


#### 5.4 Adding and loading static files

        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/main/index.html 


























































































































































