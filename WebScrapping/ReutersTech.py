from bs4 import BeautifulSoup 
import requests
import pandas as pd
import numpy as np 

headlines = []
dates = [] 

url = 'https://www.reuters.com/news/archive/technologynews?view=page&page=6&pageSize=10'

request = requests.get(url)
contents = request.content

soup = BeautifulSoup(contents, 'html.parser')

headline_news = soup.find_all('h3', class_ = 'story-title')
#description = soup.find('p')
date = soup.find_all('span', class_ = 'timestamp')

for i in range (0,len(headline_news)): 
    headlines.append(headline_news[i].text)
    dates.append(date[i].text)

    print(headlines[i].strip())
    print(dates[i].strip())














                
