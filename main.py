import schedule
import time
from weather import get_weather
from air_quality import get_air_quality
from llm_processor import analyze_weather_data
from telegram_bot import send_telegram_message

def send_daily_report():
    # 날씨 정보 가져오기
    weather_data = get_weather()
    air_quality_data = get_air_quality()
    
    # LLM으로 분석
    analysis = analyze_weather_data(weather_data, air_quality_data)
    
    # 텔레그램으로 전송
    if analysis:
        send_telegram_message(analysis)

def main():
    # 매일 아침 7시에 실행
    schedule.every().day.at("06:30").do(send_daily_report)
    
    # 테스트용: 즉시 한 번 실행
    send_daily_report()
    
    # 스케줄러 실행
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 