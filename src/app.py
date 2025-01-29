from flask import Flask, request, jsonify
from src.services.whatsapp_api import send_whatsapp_message
from src.services.deepseek_api import get_deepseek_response
from src.utils.helpers import preprocess_message
import logging
import os

app = Flask(__name__)

# Configuração de logs
logging.basicConfig(filename='../logs/bot.log', level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        user_message = data['message']
        user_number = data['from']
        processed_message = preprocess_message(user_message)
        try:
            response = get_deepseek_response(processed_message)
            send_whatsapp_message(user_number, response)
            logging.info(f"Mensagem enviada para {user_number}: {response}")
        except Exception as e:
            logging.error(f"Erro ao processar mensagem: {e}")
            send_whatsapp_message(user_number, "Desculpe, ocorreu um erro. Tente novamente mais tarde.")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)