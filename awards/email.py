from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'We are glad to have you on-board.WElcome to the family'
    sender = 'mwiksdev@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/email.txt',{"name": name})
    html_content = render_to_string('email/email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()