import certifi
import os
import ssl
from celery import shared_task
from django.core.mail import send_mail, get_connection
from django.conf import settings
import datetime

@shared_task
def send_email_task(to_email):
    """
    This function sends an email to the provided email address using Django's send_mail function.
    It is decorated with @shared_task to indicate that it is a Celery task.
    """
    context = ssl.create_default_context(cafile=certifi.where())
    
    connection = get_connection(
        backend=settings.EMAIL_BACKEND,
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS,
        fail_silently=False,
        ssl_context=context
    )

    send_mail(
        'Subject',
        'Message body',
        settings.EMAIL_HOST_USER,
        [to_email],
        connection=connection,
        fail_silently=False,
    )
    
    return 'Email sent to {}'.format(to_email)

log_dir = os.path.join(settings.BASE_DIR, 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'messaging_system.log')

@shared_task
def log_current_time():
    with open(log_file, 'a') as f:
        f.write(f"{datetime.datetime.now()}\n")
