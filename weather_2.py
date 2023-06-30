import requests

city = input("Entrez un ville : ")
api_key = "0639d9a7429e82087f5eff90fa3f34ca"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

weather = data["weather"][0]["main"]
temp = data["main"]["temp"]                   
humidity = data["main"]["humidity"]

print(f"Météo : {weather}")
print(f"Température : {temp}")
print(f"Humidité : {humidity}")                                                                 