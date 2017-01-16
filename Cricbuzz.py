# Check the score in your command Prompt ! Just replace the Url and you are done ! You'll get the score for the latest match going on !
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup


url = 'http://www.espncricinfo.com/ci/engine/match/index.html?view=live'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify())

price_box = soup.find('div',attrs={'class' : 'innings-info-1'})    # One Team Name
score = price_box.text
print(score)

price_box1 = soup.find('div',attrs={'class' : 'innings-info-2'})   # Other Team Name
score1 = price_box1.text
print(score1)

price_box2 = soup.find('div',attrs={'class' : 'match-status'})    # Match Status
status = price_box2.text
print(status)

#open a csv file with appending feature , so that old data won't get affected
with open('index.csv','a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([score,score1,status,datetime.now()])
