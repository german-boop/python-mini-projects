import requests

lat = 35.7
lon = 51.4

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print("Current Weather:")
print("Temperature:", data["current_weather"]["temperature"])
print("Wind Speed:", data["current_weather"]["windspeed"])
