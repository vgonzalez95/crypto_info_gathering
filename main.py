from flask import Flask
from data_recollector.blueprints.cryptos import cryptos

app = Flask(__name__)
app.register_blueprint(cryptos)

if __name__ == '__main__':
    app.run(debug=True)
