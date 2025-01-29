from twilio.rest import Client
from src.config import WHATSAPP_API_KEY, WHATSAPP_PHONE_NUMBER_ID

client = Client(WHATSAPP_API_KEY)

def send_whatsapp_message(to, message):
    message = client.messages.create(
        body=message,
        from_=f'whatsapp:{WHATSAPP_PHONE_NUMBER_ID}',
        to=f'whatsapp:{to}'
    )
    return message.sid