#First you need to download chromedriver (search it up) and put it into your Windows folder
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

url = "https://www.reddit.com/r/buildapcsales/new/?f=flair_name%3A%22GPU%22"
maxPrice = 500

#Open a Chrome window, scroll down a bunch, pull the HTML, and exit
options = Options()
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(2)
for i in range(1000):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
page = driver.page_source
driver.quit()

soup = BeautifulSoup(page, 'lxml')

deals = soup.find_all('a', class_ = "SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE") #HTML for each post
good_deals = []
for d in deals:
    t = d.find('h3', "_eYtD2XCVieq6emjKBH3m").text #Post title
    price = re.search('(?<=\$)[0-9,]+', t).group() #Search for first occurrence of numbers (price)
    if int(price.replace(',', '')) < maxPrice and ("AMD" in t or "RX" in t or "Radeon" in t): #Customize criteria here
        good_deals.append(t[t.find(" ")+1:] + " https://www.reddit.com/" + d['href']) #Title and link

for d in good_deals:
    print(d)