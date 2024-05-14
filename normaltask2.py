import pandas as pd
import matplotlib.pyplot as plt

daily_data=pd.read_csv("C:\\Users\\User\\Downloads\\climate.csv")

#Describes the dataset

print("\nBasic Statistics:")
print(daily_data.describe())

extreme_temperature_days = daily_data[daily_data['DailyMaximumDryBulbTemperature'] > 90]

# Display information about extreme temperature days
print("Extreme Temperature Days:")
print(extreme_temperature_days[['DATE', 'DailyMaximumDryBulbTemperature']])

#displays plot for Daily Snow Trends
plt.figure(figsize=(12, 6))
plt.plot(daily_data['DATE'], daily_data['DailySnowDepth'], label='SNOW')
plt.title('Daily Snow Trends')
plt.xlabel('Date')
plt.ylabel('Snow(inches)')
plt.legend()
plt.show()

#Displays Scatter Plot about Daily Snowfall vs. Daily Cooling Degree
plt.figure(figsize=(12, 6))
plt.scatter(daily_data['DailyCoolingDegreeDays'], daily_data['DailySnowfall'], alpha=0.5)
plt.title('Daily Snowfall vs. Daily Cooling Degree')
plt.xlabel('Daily Cooling Degree (°F)')
plt.ylabel('Daily Snowfall(inches)')
plt.show()

