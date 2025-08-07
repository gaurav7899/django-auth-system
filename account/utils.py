from django.core.mail import EmailMultiAlternatives # send email and html code
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

import threading

class SendEmailThread(threading.Thread):
    def __init__(self,email):  # use a private attribute
        threading.Thread.__init__(self)
        self.email = email

    # define run methods
    def run(self):
        self.email.send()

def send_activation_email(recipient_email,activation_url):
    subject = "Activation your account on" + settings.SITE_NAME
    from_email = "noreply@demomailtrap.co"
    to_email = [recipient_email]

    # load Html template
    html_content = render_to_string('account/activation_email.html',{'activation_url':activation_url})

    text_content = strip_tags(html_content)

    # send email
    email=EmailMultiAlternatives(subject,text_content,from_email,to_email)
    email.attach_alternative(html_content,"text/html")
    SendEmailThread(email).start()