from django.urls import path
from .views import sendmail_view, talktome_view, logs_view

urlpatterns = [
    path('sendmail/', sendmail_view, name='sendmail'),
    path('talktome/', talktome_view, name='talktome'),
    path('logs/', logs_view, name='logs'),
]
