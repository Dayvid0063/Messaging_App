import logging
from django.http import JsonResponse
from django.utils.timezone import now
from .tasks import send_email_task


logger = logging.getLogger(__name__)

def sendmail_view(request):
    """
    This view handles the /sendmail endpoint. It retrieves the 'sendmail' parameter from the request,
    queues the email sending task using Celery, and returns a JSON response.
    """
    to_email = request.GET.get('sendmail')
    if to_email: 
        send_email_task.delay(to_email)
        return JsonResponse({'status': 'Email queued'})
    return JsonResponse({'error': 'Email not provided'}, status=400)

def talktome_view(request):
    """
    This view handles the /talktome endpoint. It logs the current time to the logger and to a file,
    then returns a JSON response indicating the time has been logged.
    """
    current_time = now()
    logger.info(f"Current time: {current_time}")
    with open('/var/log/messaging_system.log', 'a') as log_file:
        log_file.write(f"{current_time}\n")
    return JsonResponse({'status': 'Time logged'})

def logs_view(request):
    """
    This view handles the /logs endpoint. It reads the contents of the log file and returns them in a JSON response.
    """
    with open('/var/log/messaging_system.log', 'r') as log_file:
        logs = log_file.read()
    return JsonResponse({'logs': logs})
