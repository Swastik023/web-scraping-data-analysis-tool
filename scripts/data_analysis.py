# scripts/data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the weather data from the CSV file
df = pd.read_csv("F:/projects/WebScrapingDataAnalysis/data/weather_data.csv")

# Data Cleaning
df['Temperature'] = df['Temperature'].str.extract('(\d+)').astype(int)

# Exploratory Data Analysis
print(df.describe())

# Data Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Day', y='Temperature')
plt.title('Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.xticks(rotation=45)
plt.savefig('F:/projects/WebScrapingDataAnalysis/reports/temperature_trend.png')
plt.show()
