# scripts/weather_scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of the weather forecast page
url = "https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=2487956c9f2e4ee4b69a5b6e21e9b2f73fa927b2c9e3aab68e002edcdc69fda7"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract data from the page
days = soup.find_all("h2", class_="DetailsSummary--daypartName--1Mebr")
temperatures = soup.find_all("span", class_="DetailsSummary--highTempValue--3Oteu")

# Create a dictionary to store the data
data = {
    "Day": [day.get_text() for day in days[:10]],  # Limiting to 10 days forecast
    "Temperature": [temp.get_text() for temp in temperatures[:10]],
    "Date": [datetime.now().strftime("%Y-%m-%d")] * 10
}

# Convert the dictionary to a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
df.to_csv("F:/projects/WebScrapingDataAnalysis/data/weather_data.csv", index=False)
