# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:22:58 2021

@author: snakk
"""

import requests
#import json
import pandas as pd 
#import time
from bs4 import BeautifulSoup as bs
import re
import os
from webscraping_beautiful_soup import makesoup

df= pd.read_csv(r"E:\Machine Learning\Webscraping\RoadAccidentsTheDailyObserver.csv")
df= df.iloc[:,1:4]   #Removing the indices
url_links= df['links']
news=[]
date=[]
time=[]
day=[]
dt=[]

for link in url_links:
    soup= makesoup(link)
    text=soup.findAll('p')[0].text
    text= re.sub(r'(^\s+)|\n+', '', text)   #Have to use + after ^\s because without + it will remove only one single whitespace
    news.append(text)                       #So the above line basically removes all the starting whitespaces and new lines
    for link in soup.findAll('div', class_='pub'):
        dates= link.find(re.compile(r'span')).text
        day_date_time= re.sub(r'Published\s*\W\s*',"",dates)
        pattern= re.compile(r'(\w+day)\W\s*(\w+\s*\w+).*at\s*(\w+.*)')
        matches= pattern.finditer(day_date_time)

    for match in matches:
        days= match.group(1)    
        dates= match.group(2)
        times= match.group(3)
        
    day.append(days)
    date.append(dates)
    time.append(times)
    dt.append(day_date_time)
    
df["News"]=news
df["day"]= day
df["date"]=date
df["time"]=time
df["time_desc"]=dt

path=r"E:\Machine Learning\Webscraping"
#print(df)
df.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver-final.csv'),index=False, encoding= 'utf-8-sig')
    