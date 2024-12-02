# utils.py

from twilio.rest import Client
from django.conf import settings

def enviar_sms(mensaje, destinatario):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        body=mensaje,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=destinatario
    )
    
    return message.sid