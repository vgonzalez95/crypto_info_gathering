import requests
from flask import Blueprint, jsonify

from data_recollect.config import config

cryptos = Blueprint('cryptos', __name__)


@cryptos.route('/cryptos/<string:crypto_ticker>')
def get_min_data(crypto_ticker):
    endpoint = f'{config.BASE_URL}/{crypto_ticker}?apikey={config.API_TOKEN}'
    response = requests.get(endpoint)
    payload = response.json()
    if not payload:
        print('bad ticker')
    print(payload)
    return jsonify(payload)
