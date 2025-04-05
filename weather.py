import requests
from config import WEATHER_API_KEY, CITY

def get_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": CITY,
        "appid": WEATHER_API_KEY,
        "units": "metric"  # 섭씨 온도 사용
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            raise Exception(f"Weather API Error: {data.get('message', 'Unknown error')} (Status code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Weather API Request Error: {e}")
    except Exception as e:
        raise Exception(f"Weather API Error: {e}") 