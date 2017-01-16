# Check the score in your command Prompt ! Just replace the Url and you are done ! You'll get the score for the latest match going on !
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


url = 'http://money.rediff.com/index.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())

price_box = soup.find('div',attrs={'class' : 'row_GL'})
score = price_box.text
print(score)

#open a csv file with appending feature , so that old data won't get affected
with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([score,datetime.now()])
