"""
ASGI config for ACEVEDO_ISIDORA_FINAL project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ACEVEDO_ISIDORA_FINAL.settings')

application = get_asgi_application()
