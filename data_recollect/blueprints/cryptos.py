import requests
from flask import Blueprint, jsonify

from data_recollect.config import config


cryptos = Blueprint('cryptos', __name__)

base_url = 'https://financialmodelingprep.com/api/v3/historical-chart/1min'


@cryptos.route('/cryptos/<string:crypto_ticker>')
def get_min_data(crypto_ticker):
    endpoint = f'{base_url}/{crypto_ticker}?apikey={config.API_TOKEN}'
    response = requests.get(endpoint)
    payload = response.json()
    print(payload)
    return jsonify(payload)
