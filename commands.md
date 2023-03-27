# Packages

Django 4.1.7
python-dotenv 1.0.0
djangorestframework 3.4.0
pytest 7.2.2
pytest-django-4.5.2
black==23.1.0
django-mptt-0.14.0
drf-spectacular-0.26.1 
coverage
pytest-cov-4.0.0
factory_boy-3.2.1 
pytest-factoryboy-2.5.1

# Commaands



pip install python-dotenv
pip install djangorestframework
pip install pytest
pip install pytest-django

#generating secret key: 
1. from django.core.management.utils import get_random_secret_key
2. print(get_random_secret key())

#schema testing
python3 manage.py spectacular --file schema.yml


