from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    #creating a message subject and sender
    subject='Welcome to Lifehacks'
    sender='gwan.watchlist@gmail.com'

    #passing in the context variables
    text_content=render_to_string('email/newsemail.txt',{"name":name})
    html_content=render_to_string('email/newsemail.html',{"name":name})

    msg=EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'txt/html')
    msg.send()
