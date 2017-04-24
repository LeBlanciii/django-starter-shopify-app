import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-starter-shopify-app.settings")

application = get_wsgi_application()
