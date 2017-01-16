# Check the score in your command Prompt ! Just replace the Url and you are done ! You'll get the score for the latest match going on !
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


url = 'http://www.accuweather.com/en/in/bengaluru/204108/current-weather/204108'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())

price_box = soup.find('div',attrs={'class' : 'bg bg-cl'})
score = price_box.text
print(score)

price_box2 = soup.find('div',attrs={'class' : 'bg bg-su'})
score1 = price_box.text
print(score1)

price_box2 = soup.find('div',attrs={'class' : 'bg bg-su'})
score2 = price_box.text
print(score2)

#open a csv file with appending feature , so that old data won't get affected
with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([score,score1,score2,datetime.now()])
