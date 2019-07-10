import json, datetime, requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol=BTC'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '2ab61a36-baba-4c63-895e-378f149bf2b9',
}

session = Session()
session.headers.update(headers)

cmc_key = "2ab61a36-baba-4c63-895e-378f149bf2b9"
global_url = 'https://api.coinmarketcap.com/v2/ticker/'
history_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

# Get current rate
def get_current_rate(name):
		name = name.upper()
		response = requests.get(global_url).json()

		for i in response['data'].values():
			if i['symbol'] == name:
				return json.dumps({name: i['quotes']['USD']['price']})


#Get previous BTC rate
def get_previous_rate(date):
	if request.method == 'POST':
		response = requests.get(history_url).json()

		for i in response['bpi']:
			if date in i:
				return json.dumps({i: response['bpi'][i], 'symbol': 'BTC'})

		
def convert_usd_to_uah(price):
  bank_url = 	'http://bank-ua.com/export/exchange_rate_cash.json'
 	response = requests.get(bank_url).json()

	for i in response:
		if i['bankName'] == 'ПриватБанк' and i['codeAlpha'] == 'USD':
			rate_usd = i['rateSale']

	rate_bitcoin = float(rate_usd) * float(price)
	print('Rate: {} uah'.format(rate_bitcoin))
