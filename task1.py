import requests
import matplotlib.pyplot as plt

API_KEY = "ab6f61f9d233c5b3ff024d0fba152411"
CITY = "London"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

dates = [item['dt_txt'] for item in data['list'][:10]]
temps = [item['main']['temp'] for item in data['list'][:10]]

plt.figure(figsize=(10,5))
plt.plot(dates, temps, marker='o')
plt.xticks(rotation=45)
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()