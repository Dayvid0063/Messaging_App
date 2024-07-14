# DevOpsStage3Task: Messaging System with RabbitMQ/Celery and Python Application behind Nginx

## Objective

Deploy a Python application behind Nginx that interacts with RabbitMQ/Celery for email sending and logging functionality.

## Requirements

### Local Setup

1. **Install RabbitMQ and Celery**

   - Install RabbitMQ 
     ```bash
     sudo apt-get update
     sudo apt-get install -y rabbitmq-server
     sudo systemctl enable rabbitmq-server
     sudo systemctl start rabbitmq-server
     ```
   - Install Celery using pip:
     ```bash
     pip install celery
     ```

2. **Install Django**

   - Install Django in your virtual environment:
     ```bash
     python -m pip install django
     ```

3. **Create requirements.txt**

   - Generate requirements.txt for version control:
     ```bash
     python -m pip freeze > requirements.txt
     ```

4. **Create Django Project**

   - Initialize a Django project:
     ```bash
     django-admin startproject Messaging_App .
     ```

5. **Start Django App**

   - Create a Django app within the project:
     ```bash
     python manage.py startapp rcp_app
     ```

### Endpoint Functionalities

1. **?sendmail Endpoint**

   - Sends an email using SMTP to the provided email address (`?sendmail=destiny@destinedcodes.com`).
   - Uses RabbitMQ/Celery to queue the email sending task.
   - Ensure the email-sending script retrieves and executes tasks from the queue.

2. **?talktome Endpoint**

   - Logs the current time to `/var/log/messaging_system.log`.

### Nginx Configuration

1. **Configure Nginx**

   - Install Nginx if not already installed.
   - Configure Nginx to serve your application.
   - Ensure proper routing of requests to the application endpoints (`?sendmail` and `?talktome`).

### Endpoint Access

1. **Expose Local Application Endpoint**

   - Use ngrok or a similar tool to expose your local application endpoint for external access.
   - Provide a stable endpoint URL for testing purposes.


## Conclusion

Follow these steps to successfully deploy your Python application with RabbitMQ/Celery behind Nginx, covering email sending and logging functionalities.

## Author

- David ORJI
