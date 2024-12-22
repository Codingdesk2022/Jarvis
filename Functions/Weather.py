from Lib.Libraries import *
from Utils.SpeechDrive import *
from APIs.weatherAPIKey import *

def weather():
    city = "allahabad"
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no")
    forecast = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&aqi=no")      
    response.raise_for_status()  # Check if request was successful
    forecast.raise_for_status()
    forecast_response = forecast.json()
    weather = response.json()['current']['condition']['text']
    wind = response.json()['current']['wind_kph']
    min_temp_f = forecast_response['forecast']['forecastday'][0]['day']['mintemp_f']
    max_temp_f = forecast_response['forecast']['forecastday'][0]['day']['maxtemp_f']
    min_temp_c = (min_temp_f - 32) * 5.0 / 9.0
    max_temp_c = (max_temp_f - 32) * 5.0 / 9.0
    print(f"Today’s forecast reveals a {weather} day ahead. Anticipate a high temperature of {max_temp_c:.2f}°C and a low of {min_temp_c:.2f}°C. Wind speeds will reach {wind} kilometers per hour.")
    speak(f"Today’s forecast reveals a {weather} day ahead. Anticipate a high temperature of {max_temp_c:.2f}°C and a low of {min_temp_c:.2f}°C. Wind speeds will reach {wind} kilometers per hour.")