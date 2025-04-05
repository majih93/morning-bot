import requests
from config import AIR_QUALITY_API_KEY, CITY

def get_air_quality():
    base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "q": CITY,
        "appid": AIR_QUALITY_API_KEY
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            aqi = data["list"][0]["main"]["aqi"]
            components = data["list"][0]["components"]
            
            air_quality_info = {
                "aqi": aqi,
                "pm2_5": components["pm2_5"],
                "pm10": components["pm10"],
                "co": components["co"],
                "no2": components["no2"],
                "so2": components["so2"]
            }
            return air_quality_info
        else:
            return None
    except Exception as e:
        print(f"Air Quality API Error: {e}")
        return None 