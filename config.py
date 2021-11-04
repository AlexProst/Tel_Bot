import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
URL_Turkmenistan = os.getenv('URL_Turkmenistan')
URL_Bellarus = os.getenv('URL_Bellarus')
URL_Afganistan = os.getenv('URL_Afganistan')

print(BOT_TOKEN)