from weather import get_weather
from air_quality import get_air_quality
from llm_processor import analyze_weather_data
from telegram_bot import send_telegram_message
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_once():
    try:
        logger.info("Starting daily weather report...")
        
        # 날씨 정보 가져오기
        logger.info("Fetching weather data...")
        weather_data = get_weather()
        if not weather_data:
            logger.error("Failed to get weather data")
            return
        
        # 대기질 정보 가져오기
        logger.info("Fetching air quality data...")
        air_quality_data = get_air_quality()
        if not air_quality_data:
            logger.error("Failed to get air quality data")
            return
        
        # LLM으로 분석
        logger.info("Analyzing data with LLM...")
        analysis = analyze_weather_data(weather_data, air_quality_data)
        if not analysis:
            logger.error("Failed to analyze data")
            return
        
        # 텔레그램으로 전송
        logger.info("Sending message to Telegram...")
        if send_telegram_message(analysis):
            logger.info("Message sent successfully!")
        else:
            logger.error("Failed to send message to Telegram")
            
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    run_once() 