#The Standard & Poor's 500, often abbreviated as the S&P 500,
#or just "the S&P", is an American stock market index based on the market capitalizations of 500 large companies
#having common stock listed on the NYSE or NASDAQ. The S&P 500 index components and
#their weightings are determined by S&P Dow Jones Indices.

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


url = 'https://www.bloomberg.com/quote/SPX:IND'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html.parser")

name_box = soup.find('h1',attrs={'class' : 'name'})
name = name_box.text.strip()
print(name)

price_box = soup.find('div',attrs={'class' : 'price'})
price = price_box.text
print(price)

#open a csv file with appending feature , so that old data won't get affected
with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name,price,datetime.now()])
