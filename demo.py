import datetime, requests, yfinance
from alpaca_trade_api.rest import REST
from getpass import getpass

BASE_URL="https://paper-api.alpaca.markets"
API_KEY = "PK2VQM34GZV9THDD5EM2"
SECRET_KEY ="ITtLKBlrJu3RbfRdAHeB6VsBL10y54GfAv7LN1hM"

api = REST(key_id=API_KEY, secret_key=SECRET_KEY, base_url=BASE_URL)

news = api.get_news('TSLA')
