# config.py
# config.py

# Configurações da API da DeepSeek
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"  # Modelo de linguagem a ser utilizado
DEEPSEEK_TEMPERATURE = 0.7  # Parâmetro de criatividade (0 a 1)
DEEPSEEK_MAX_TOKENS = 150  # Número máximo de tokens na resposta

# Configurações do WhatsApp (Twilio)
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Número do Twilio Sandbox
TWILIO_API_URL = "https://api.twilio.com/2010-04-01/Accounts/{AccountSID}/Messages.json"

# Configurações do Bot
BOT_NAME = "Atendente Virtual"
BOT_LANGUAGE = "pt-BR"  # Idioma padrão do bot
BOT_RESPONSE_DELAY = 2  # Tempo de espera (em segundos) para simular um atendimento humano

# Configurações de Log
LOG_FILE = "logs/bot.log"  # Caminho para o arquivo de log
LOG_LEVEL = "INFO"  # Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# Configurações de Ambiente
ENVIRONMENT = "development"  # Ambiente de execução (development, production)
DEBUG = True  # Modo de depuração (True para desenvolvimento, False para produção)