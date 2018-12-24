import requests
import pandas
import os

def get_buffetRule(input_tickers=['APPL', 'AMZN', 'GOOG']):
	'''
	Input: List of Stocks
	Output (float): Market Capitalisation / Gross Revenue

	'''
	for ticker in input_tickers:
		url = 'https://finance.yahoo.com/quote/{}/'.format(ticker)
		r = requests.get(url)
		print(r.text)

