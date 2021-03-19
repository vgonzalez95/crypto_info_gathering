from flask import Flask
from data_recollect.blueprints.cryptos import cryptos


def main():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')
    app.register_blueprint(cryptos)
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
