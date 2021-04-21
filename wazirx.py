#!/usr/bin/env python3
import requests
import json
import time
import sys
from texttable import Texttable
from os import system
clear = lambda: system('clear')

while True:
	try:
		time.sleep(2)	#to stop the screen
		clear()	#clear the previous data from the screen to display the updated values
		config = open('st','r')
		data = config.readlines()
		all_coin=[["Coin","QTY","BUY","TOTAL","SELL","TOTAL","P&L"]]  #headers for the table
		for val in data:
			coin =val.split()
			url="https://api.wazirx.com/api/v2/trades?market={0}".format(coin[0])
			response = requests.get(url).json()
			response = response[0]
			#print(response['price'])		
			coin.append(float(coin[1])*float(coin[2])) #total price you purchased
			coin.append(float(response['price']))
			coin.append(float(response['price'])*float(coin[1])) #total sell price
			coin.append(coin[5]-coin[3]) #total p&l
			all_coin.append(coin)
		b_total ,s_total,p_total = 0,0,0
		#adding total buy price, sell price and total P&L
		for data in all_coin[1:]:
			b_total = b_total + int(data[3])
			s_total = s_total + int(data[5])
			p_total = p_total + int(data[6])
		last_row = ['','','',b_total,'',s_total,p_total]
		all_coin.append(last_row)
		l = all_coin
		table = Texttable()
		table.add_rows(l) 
		print(table.draw())
		config.close()
	except:
		print('something went wrong')

