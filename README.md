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


#### 5.5 Adding home page template using template inheritance

        modified:   README.md
        new file:   templates/base.html
        new file:   templates/main/inc/banner-brands.html
        new file:   templates/main/inc/banner-customer-services.html
        new file:   templates/main/inc/banner-customer-support.html
        new file:   templates/main/inc/banner-promo.html
        new file:   templates/main/inc/product-widgets.html
        new file:   templates/main/inc/side-menu.html
        new file:   templates/main/inc/side-newsletter.html
        new file:   templates/main/inc/side-slider-blog-post.html
        new file:   templates/main/inc/side-slider-comments.html
        new file:   templates/main/inc/side-slider-sale.html
        new file:   templates/main/inc/slider-featured-products.html
        new file:   templates/main/inc/slider-home.html
        modified:   templates/main/index.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header-top.html
        new file:   templates/shared/header.html
        new file:   templates/shared/menu-mobile.html
        new file:   templates/shared/newsletter-popup.html
        new file:   templates/shared/topbar-promo.html


#### 5.6 Create product app

        modified:   README.md
        new file:   apps/product/__init__.py
        new file:   apps/product/admin.py
        new file:   apps/product/apps.py
        new file:   apps/product/migrations/__init__.py
        new file:   apps/product/models.py
        new file:   apps/product/tests.py
        new file:   apps/product/views.py
        modified:   config/settings.py


#### 5.7 Creating product list template (Views, Template, Urls)

        modified:   README.md
        modified:   apps/main/urls.py
        new file:   apps/product/urls.py
        modified:   apps/product/views.py
        modified:   config/urls.py
        modified:   templates/base.html
        new file:   templates/product/product-list.html
        modified:   templates/shared/header-top.html


#### 5.8 Adding category-list page and sagmenting the product-list and category-list pages

        modified:   README.md
        modified:   apps/product/urls.py
        modified:   apps/product/views.py
        modified:   templates/base.html
        new file:   templates/product/category-list.html
        new file:   templates/product/inc/benner-top-promo.html
        new file:   templates/product/inc/breadcrumb.html
        new file:   templates/product/inc/content.html
        new file:   templates/product/inc/nav-pagination.html
        new file:   templates/product/inc/nav-toolbox.html
        new file:   templates/product/inc/side-brand.html
        new file:   templates/product/inc/side-category.html
        new file:   templates/product/inc/side-color.html
        new file:   templates/product/inc/side-custom-widget.html
        new file:   templates/product/inc/side-featured.html
        new file:   templates/product/inc/side-price.html
        new file:   templates/product/inc/side-size.html
        modified:   templates/product/product-list.html
        modified:   templates/shared/header-top.html



### -----------------------------------------------
### 6. WORKING ON MODELS, VIEWS TEMPLATE AND URLS
### -----------------------------------------------


#### 6.1 Create Category and Product models with ManyToOne Rel

        modified:   README.md
        modified:   apps/product/admin.py
        new file:   apps/product/migrations/0001_initial.py
        modified:   apps/product/models.py


#### 6.2 Add and Read CATEGORY-BASED PRODUCTS

        modified:   README.md
        modified:   apps/product/models.py
        modified:   apps/product/urls.py
        modified:   apps/product/views.py
        modified:   templates/base.html
        modified:   templates/product/inc/content.html
        modified:   templates/product/inc/side-category.html
        modified:   templates/product/product-list.html
        modified:   templates/shared/head.html
        modified:   templates/shared/header-top.html












































































































































