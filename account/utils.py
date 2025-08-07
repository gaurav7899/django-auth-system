from django.core.mail import EmailMultiAlternatives # send email and html code
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

import threading

class SendEmailThread(threading.Thread):
    def __init__(self,email):
        threading.Thread.__init__(self)

    # define run methods
    def run(self):
        self.email.send()

def send_activation_emial(recipient_email,activation_url):
    subject = "Activation your account on" + settings.SITE_NAME
    from_email = "noreply@somting.com"
    to_email = [recipient_email]

    # load Html template
    html_render = render_to_string('account/activation_email.html',{'activation_url':activation_url})