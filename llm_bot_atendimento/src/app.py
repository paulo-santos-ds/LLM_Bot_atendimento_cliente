from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import llm_bot_atendimento.src.config as config  # Importar configurações

app = Flask(__name__)

# Configurações da API da DeepSeek (carregadas do config.py)
DEEPSEEK_API_URL = config.DEEPSEEK_API_URL
DEEPSEEK_API_KEY = config.DEEPSEEK_API_KEY

# Função para enviar mensagem para a API da DeepSeek
def get_deepseek_response(user_message):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Desculpe, ocorreu um erro ao processar sua solicitação."

# Rota para receber mensagens do WhatsApp
@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_message = request.form.get('Body')
    from_number = request.form.get('From')

    # Processar a mensagem com a API da DeepSeek
    deepseek_response = get_deepseek_response(incoming_message)

    # Enviar a resposta de volta ao WhatsApp
    resp = MessagingResponse()
    resp.message(deepseek_response)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)