
# Web Scraping and Data Analysis Tool

This project is a web scraping and data analysis tool that scrapes weather data from Weather.com, processes and analyzes the data, and generates reports.

## Project Structure

```
F:\projects\WebScrapingDataAnalysis
├── data
│   └── weather_data.csv         # CSV file to store scraped weather data
├── scripts
│   ├── weather_scraper.py       # Script for scraping weather data
│   ├── data_analysis.py         # Script for analyzing and visualizing data
│   └── automation.py            # Script for automating the entire process
├── reports
│   └── temperature_trend.png    # Image file for the temperature trend visualization
├── venv                         # Virtual environment directory
│   ├── Include
│   ├── Lib
│   ├── Scripts
│   ├── pyvenv.cfg
│   └── ...                      # Other virtual environment files and directories
├── .gitignore
├── README.md                    # Project documentation and setup instructions
└── Documentation.pdf            # Comprehensive PDF with project details, code, and interview Q&A
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Set up a virtual environment:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```
4. Install the required libraries:
    ```sh
    pip install requests beautifulsoup4 pandas matplotlib seaborn apscheduler
    ```

## Usage Instructions

1. Run the weather scraper script:
    ```sh
    python scripts/weather_scraper.py
    ```
2. Run the data analysis script:
    ```sh
    python scripts/data_analysis.py
    ```
3. To automate the process, run the automation script:
    ```sh
    python scripts/automation.py
    ```

## Code Explanation

### weather_scraper.py

This script scrapes the weather forecast from Weather.com and saves the data to a CSV file.

### data_analysis.py

This script loads the weather data, cleans it, performs exploratory data analysis, and visualizes the temperature trend.

### automation.py

This script automates the web scraping and data analysis process, scheduling it to run once a day.
