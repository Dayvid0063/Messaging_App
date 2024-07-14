from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messaging_App.settings')

app = Celery('Messaging_App')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['rcp_app'])


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
