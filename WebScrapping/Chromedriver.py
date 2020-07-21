import io
import tweepy 
from bs4 import BeautifulSoup 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dateutil.parser
from datetime import datetime 

drive = webdriver.Chrome(chromedriver.exe)

driver.get('https://www.reuters.com/news/archive/businessnews?view=page&page=5&pageSize=10')

count = 0
headlines = []
dates = []

for x in range(500): 

    try: 

        loadMoreButton = driver.find_element_by_class_name("control-nav-next")
        time.sleep(3)

        loadMoreButton.click() 
        time.sleep(2)

        news_headlines = driver.find_element_by_class_name("story-title")
        news_dates = drive.find_element_by_class_name("timestamp")

        for headline in news_headlines: 
            headlines.append(headline.text)
            print(headlines.text)
        
        for date in news_dates: 
            dates.append(date.text)
            print(date.text)

        count = count +1 
        print("CLICKED")
    
    except Exception as e: 
        print(e)
        break 

    








