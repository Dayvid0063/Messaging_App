from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported
from .celery_app import app as celery_app

__all__ = ('celery_app',)
