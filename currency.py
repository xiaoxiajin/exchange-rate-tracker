import requests
from datetime import datetime, timedelta
import json
import os


class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.data_file = 'data.json'

        # Ensure data file exists
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump({}, f)

    def fetch_and_save_rate(self, fetch_date=None):
        """Fetches today's rate and saves it."""
        if fetch_date is None:
            fetch_date = datetime.now().strftime('%Y-%m-%d')

        self.url = f'https://api.exchangeratesapi.io/v1/{fetch_date}?access_key={
            self.api_key}'

        res = requests.get(self.url)
        if res.status_code == 200:
            res_json = res.json()
            cny_rate = res_json['rates'].get('CNY')

            if cny_rate is None:
                print(f"No rate found for CNY on {fetch_date}.")

            # Save rate to file
            try:
                with open(self.data_file, 'r+') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = {}

                    data[fetch_date] = cny_rate

                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()

            except FileNotFoundError:
                with open(self.data_file, 'w') as f:
                    data = {fetch_date: cny_rate}
                    json.dump(data, f, indent=4)
                print(
                    f"File created and rate for {fetch_date} saved: {cny_rate}")
        else:
            print(
                f"Failed to fetch rate for {fetch_date}. Status code: {res.status_code}")

    def generate_range_data(self, start_date, end_date):
        """Generates exchange rate data for a range of dates."""
        # Convert strings to datetime objects
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Iterate through each date in the range
        current = start
        while current <= end:
            fetch_date = current.strftime("%Y-%m-%d")
            self.fetch_and_save_rate(fetch_date)
            current += timedelta(days=1)

    def get_min_max_rate(self, start_date, end_date):
        """Returns the min and max rates in the specified date range."""
        with open(self.data_file, 'r') as f:
            data = json.load(f)

        # Filter data within the date range
        rates = {date: rate for date, rate in data.items() if start_date <=
                 date <= end_date}

        if not rates:
            return {"error": "No data available for the given range."}

        min_date = min(rates, key=rates.get)
        max_date = max(rates, key=rates.get)

        return {
            "min_rate": {"date": min_date, "rate": rates[min_date]},
            "max_rate": {"date": max_date, "rate": rates[max_date]}
        }
