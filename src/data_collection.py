from pytrends.request import TrendReq
import pandas as pd
import os

# Initialize pytrends connection
pytrends = TrendReq(hl='en-US', tz=360)

# Define keywords for sports activities# data_collection.py

from pytrends.request import TrendReq
import pandas as pd
import os
import time

# Initialize pytrends connection
pytrends = TrendReq(hl='en-US', tz=360)

# Define keywords for sports activities
keywords = ["running", "cycling", "swimming", "yoga", "gym"]

# Build payload for Google Trends
pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')

# Fetch interest over time with error handling
try:
    data = pytrends.interest_over_time()

    # Check if data contains the required columns and drop 'isPartial' if it exists
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])

    # Check if the data is empty
    if data.empty:
        print("No data retrieved. Exiting.")
    else:
        # Ensure the data directory exists
        os.makedirs("../data", exist_ok=True)

        # Save to CSV
        output_file = "../data/trends.csv"
        data.to_csv(output_file)

        print(f"Data successfully collected and saved to {output_file}.")

except Exception as e:
    print(f"An error occurred while fetching the data: {e}")
    time.sleep(30)  # Wait 30 seconds before retrying (you can add more retries if needed)

keywords = ["running", "cycling", "swimming", "yoga", "gym"]

# Build payload for Google Trends
pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')

# Fetch interest over time
data = pytrends.interest_over_time()

# Check if data contains the required columns
if 'isPartial' in data.columns:
    data = data.drop(columns=['isPartial'])

# Ensure the data directory exists
os.makedirs("../data", exist_ok=True)

# Save to CSV
output_file = "../data/trends.csv"
data.to_csv(output_file)

print(f"Data successfully collected and saved to {output_file}.")
