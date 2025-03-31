from twilio.rest import Client

# Substitua pelos seus dados do Twilio
account_sid = 'Gabriel'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Olá! Como posso ajudá-lo?",
    from_='whatsapp:+14155238886',  # Número Twilio WhatsApp
    to='whatsapp:+5511999999999'  # Número de destino
)

print(message.sid)
