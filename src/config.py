import os
import pandas
from dotenv import load_dotenv

load_dotenv()


#conexoes
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
WHATSAPP_API_KEY = os.getenv('WHATSAPP_API_KEY')
WHATSAPP_PHONE_NUMBER_ID = os.getenv('WHATSAPP_PHONE_NUMBER_ID')