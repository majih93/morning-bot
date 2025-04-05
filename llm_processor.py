from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_weather_data(weather_data, air_quality_data):
    if not weather_data or not air_quality_data:
        return "데이터를 가져오는 중 오류가 발생했습니다."
    
    prompt = f"""
    다음은 현재 날씨와 대기질 정보입니다. 이 정보를 바탕으로 오늘의 날씨와 대기질 상태를 분석하고, 
    일상생활에 도움이 되는 조언을 제공해주세요. 한국어로 답변해주세요.
    
    날씨 정보:
    - 온도: {weather_data['temperature']}°C
    - 습도: {weather_data['humidity']}%
    - 날씨 상태: {weather_data['description']}
    - 풍속: {weather_data['wind_speed']} m/s
    
    대기질 정보:
    - 대기질 지수 (AQI): {air_quality_data['aqi']}
    - PM2.5: {air_quality_data['pm2_5']} μg/m³
    - PM10: {air_quality_data['pm10']} μg/m³
    - 일산화탄소: {air_quality_data['co']} μg/m³
    - 이산화질소: {air_quality_data['no2']} μg/m³
    - 이산화황: {air_quality_data['so2']} μg/m³
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides weather and air quality analysis in Korean."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "분석 중 오류가 발생했습니다." 