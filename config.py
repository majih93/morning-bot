import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Weather API
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
CITY = "Seoul"  # 기본 도시 설정

# Air Quality API
AIR_QUALITY_API_KEY = os.getenv('AIR_QUALITY_API_KEY') 