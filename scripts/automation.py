# scripts/automation.py

import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    # Run the weather scraper script
    subprocess.run(["python", "F:/projects/WebScrapingDataAnalysis/scripts/weather_scraper.py"])
    # Run the data analysis script
    subprocess.run(["python", "F:/projects/WebScrapingDataAnalysis/scripts/data_analysis.py"])

# Create a scheduler
scheduler = BlockingScheduler()
# Schedule the job to run once a day
scheduler.add_job(job, 'interval', days=1)
scheduler.start()
