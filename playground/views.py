from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customer


def say_hello(request):
    notify_customer.delay('Hello')
    # try:
    #     email_massage = BaseEmailMessage(template_name='emails/email.html', context={'name': 'Umut'})
    #     email_massage.send(['basak@hopebuy.com'])
    # except BadHeaderError:
    #     pass
    return render(request, 'hello.html', {'name': 'Umut'})
