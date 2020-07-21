from bs4 import BeautifulSoup 
import requests
import pandas as pd
import numpy as np 
import tweepy

auth = tweepy.OAuthHandler("O8WB9EZCOxo9ex1cTJb6yfbBz", "DDVOMEpV3JInQRZsXeX7ok7edlgzb4EF2kcZJtTE8lrtSIzuSq")
auth.set_access_token("1073725176364306432-5mPKGUXbMBedcYnWiM3OcvfXl5cyoO", "rgI1QHf8M7qkEKIXfd0VhDOMxexqgxmp4ApoLrFtcd9V2")
api = tweepy.API(auth)

try: 
    api.verify_credentials()
    print("DOne")
except: 
    print("ERROR")

headlines = []

R_URLS=['https://www.reuters.com/news/world',
     'https://www.reuters.com/places/mexico',
     'https://www.reuters.com/finance/deals',
     'https://www.reuters.com/subjects/banks',
     'https://www.reuters.com/finance/markets',
     'https://www.reuters.com/finance/markets/europe',
     'https://www.reuters.com/finance/markets/asia',
     'https://www.reuters.com/news/technology',
     'https://www.reuters.com/politics',
     'https://www.reuters.com/places/brazil',
     'https://www.reuters.com/places/russia',
     'https://www.reuters.com/subjects/euro-zone',
     'https://www.reuters.com/subjects/middle-east',
     'https://www.reuters.com/places/japan',
     'https://www.reuters.com/places/china',
     'https://www.reuters.com/places/africa',
     'https://www.reuters.com/breakingviews']
     
     
S_URLS = ['https://www.wsj.com/news/world']

"""
for link in R_URLS: 
    request = requests.get(link)
    contents = request.content
    soup = BeautifulSoup(contents, 'html.parser')
    headline_news = soup.find_all('h3', class_ = 'story-title')

    for i in range (0,len(headline_news)): 
        headlines.append(headline_news[i].text)
        
        
for i in range(0, len(headlines)):        
    tweet = headlines[i].strip()
    
    try:
        #api.update_status(tweet)
        print(tweet)
    except: 
        print("Tweet Failed")
"""      
    
for link in S_URLS: 
    request = requests.get(link)
    contents = request.content
    soup = BeautifulSoup(contents, 'html.parser')
    headline_news = soup.find_all('a')

    for i in range (0,len(headline_news)): 
        headlines.append(headline_news[i].text)
        
        
for i in range(0, len(headlines)):        
    tweet = headlines[i].strip()
    
    try:
        #api.update_status(tweet)
        print(tweet)
    except: 
        print("Tweet Failed")
    














                
                
                
                
                
