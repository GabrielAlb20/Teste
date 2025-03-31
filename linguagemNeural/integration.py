from twilio.rest import Client
from flask import Flask, request

# Inicializar o app Flask
app = Flask(__name__)

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

def predict_message(message):
    # Função para gerar resposta (pode ser adaptada para modelos complexos)
    if "olá" in message.lower():
        return "Oi, como posso ajudar?"
    else:
        return "Desculpe, não entendi. Pode reformular?"

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')

    response_msg = predict_message(incoming_msg)

    message = client.messages.create(
        body=response_msg,
        from_='whatsapp:+14155238886',
        to=from_number
    )

    return '', 200

if __name__ == "__main__":
    app.run(debug=True)
