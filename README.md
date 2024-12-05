# Exchange Rate Tracker

This project tracks the exchange rates of Euro (EUR) to Chinese Yuan (CNY) over a specified date range. The rates are fetched using a public API and stored in a `data.json` file for easy access and analysis.

## Files

- **`data.json`**: This file contains exchange rates for specific dates. The data is generated using the `currency.py` file, which fetches the exchange rates and stores them.
- **`app.py`**: The main backend of the project, built using Flask. It provides a POST endpoint (`/rates`) that accepts a date range and returns the minimum and maximum exchange rates for that period.
- **`currency.py`**: Contains the logic for fetching and storing exchange rates, as well as generating exchange rate data for a specific date range.
- **`index.html`**: The frontend of the project. A simple form allows the user to input a date range and view the min/max exchange rates.
- **`styles.css`**: The CSS styles for the frontend to ensure the elements are well aligned and visually appealing.
- **`script.js`**: JavaScript file that handles the form submission and fetches the exchange rates from the Flask API.

## API Data

Currently, due to API usage limitations, the exchange rate data in the `data.json` file ranges from **2024-01-01** to **2024-03-04**. The file is updated periodically by running the `generate_range_data` function from `currency.py`.

## How to Run Locally

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/exchange-rate-tracker.git
   cd exchange-rate-tracker
   Install the required dependencies:
   ```

2. Make sure you have Python 3 and pip installed.
   Install Flask using pip:
   `pip install flask flask-cors requests`

3. Run the Flask app:
   `python app.py`

4. Open index.html in your browser. You can also open it directly or run a local server for better experience .

## How to Fetch and Save Data

To generate new exchange rate data, you can run the following command in the currency.py file.
e.g.

```
currency = Currency()
currency.generate_range_data("2024-01-01", "2024-03-04")
```

This will update the data.json file with the new data.

Note: api key available from https://exchangeratesapi.io/documentation/, save as api_key to run the file
