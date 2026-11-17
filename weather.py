import requests
import pandas as pd
url = "https://api.open-meteo.com/v1/forecast"

params = {
"latitude": 32.08,
 "longitude": 34.78,
  "hourly": "temperature_2m",
   "forecast_days": 3
}

response = requests.get(url, params=params, timeout=10)

assert response.status_code == 200

response.raise_for_status()
data = response.json()

hourly = data['hourly']

df = pd.DataFrame({
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"]
})

print(df.head())

print("Average temperature:", df.temperature.mean())
print("Highest temperature:", df.temperature.max())
print("Lowest temperature:", df.temperature.min())
print("Variance:", df.temperature.var())
print("Standard deviation:", df.temperature.std())