import requests

api_key = "0639d9a7429e82087f5eff90fa3f34ca"
lat = "37.532600"
lon = "127.024612"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
temp = data["main"]["temp"]
print(f"La température à Séoul est de {temp} degré Celsius.")

                                                                                                                                                                                      