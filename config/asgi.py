"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_app = get_asgi_application()
application = FastAPI()

@application.get("/api")
async def api_root():
    return {"message": "Hello from FastAPI"}

application.mount("/django", WSGIMiddleware(django_app))

