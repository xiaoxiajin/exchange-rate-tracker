from flask import Flask, request, jsonify
from currency import Currency
from flask_cors import CORS

app = Flask(__name__)
currency = Currency()
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})


@app.route('/rates', methods=['POST'])
def get_rates():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Invalid date range"}), 400

    result = currency.get_min_max_rate(start_date, end_date)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
