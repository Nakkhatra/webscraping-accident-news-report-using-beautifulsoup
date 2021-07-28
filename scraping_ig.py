# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 03:33:11 2021

@author: snakk
"""

import requests
from bs4 import BeautifulSoup as bs

url= 'https://www.instagram.com/direct/t/340282366841710300949128143720569628636'


def makesoup(url):
    response= requests.get(url)
    doc= requests.get(url)
    
    if True:
        soup = bs(response.content, 'lxml')
        print(f'received url:{url}')
    #else:
        #print(f"{url} cannot be reached.")
        
    return soup

soup= makesoup(url)

