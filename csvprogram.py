import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Weather_data.csv')
data['date'] = pd.to_datetime(data['date'])

plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temperature'], marker='o')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_plot.png')
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(data['date'], data['humidity'], c='blue')
plt.title('Humidity Over Time')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('humidity_scatter_plot.png')
plt.show()
