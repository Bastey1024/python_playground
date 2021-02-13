import requests

API_KEY="6b8ee41d96596b0e44d4dfb48d4f7a87"
response = requests.get(f"api.openweathermap.org/data/2.5/weather?q=Hamburg&appid={API_KEY}")
data = response.json()

print(data)
