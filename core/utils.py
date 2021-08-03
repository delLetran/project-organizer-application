from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import (
  get_object_or_404
)
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django_q.tasks import async_task
# from django_q.tasks import result, fetch

User = get_user_model()

def SendEmailVerification(email, username, encoded_id, token, *args, **kwargs ):
  context = {
    'username': username,
    'email': email,
    'encoded_id': encoded_id,
    'token': token
  }
  message = render_to_string('user/email_verification.html', context)
  formated_mail = EmailMultiAlternatives(
    "Account Verification",
    message,
    settings.EMAIL_HOST_USER,
    [email, 'delio.letran@gmail.com',]
  )
  formated_mail.attach_alternative(message, 'text/html')
  formated_mail.send()

def sendAsycnMail(email, token, *args, **kwargs ):
  user = get_object_or_404(User, email=email)
  encoded_id = urlsafe_base64_encode(force_bytes(user.pk))
  task_id = async_task(SendEmailVerification, email, user, encoded_id, token)
  return task_id


def is_str(data):
  return (type(data) == str)















# def get_task_result(task_id):
#   task = fetch(task_id)
#   return result(task, wait=1000)


# if settings.DEBUG:
#   SYNC=True
# else:
#   SYNC=False

# def sendMail(username, email, token, *args, **kwargs ):
#   user = get_object_or_404(User, username=username)
#   encoded_id = urlsafe_base64_encode(force_bytes(user.pk))
#   task_id = async_task(SendEmailVerification, username, email, encoded_id, token, sync=SYNC)
#   task = fetch(task_id)
#   if task.success:
#     return {'result':'Email verification sent', 'status':200}
#   return {'result':'An error has occured', 'status':408}
