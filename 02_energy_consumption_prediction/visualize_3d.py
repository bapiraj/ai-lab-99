import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("energy_consumption_data.csv")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['temperature_celsius'], df['humidity_percent'], df['energy_consumption_kwh'], alpha=0.7)

ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Humidity (%)')
ax.set_zlabel('Energy Consumption (kWh)')
ax.set_title('Temperature, Humidity vs Energy Consumption')

plt.show()
