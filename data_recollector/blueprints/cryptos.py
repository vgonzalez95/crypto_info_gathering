from flask import Blueprint, jsonify
import requests

cryptos = Blueprint('cryptos', __name__)

api_key = 'fdc87acc05b63069ece12db7d63a9541'
base_url = f'https://financialmodelingprep.com/api/v3/historical-chart/1min'

###
@cryptos.route('/cryptos/<string:crypto_ticker>')
def get_min_data(crypto_ticker):
    endpoint = f'{base_url}/{crypto_ticker}?apikey={api_key}'
    response = requests.get(endpoint)
    payload = response.json()
    print(payload)
    return jsonify(payload)
