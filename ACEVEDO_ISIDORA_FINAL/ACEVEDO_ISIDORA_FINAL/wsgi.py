"""
WSGI config for ACEVEDO_ISIDORA_FINAL project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ACEVEDO_ISIDORA_FINAL.settings')

application = get_wsgi_application()
