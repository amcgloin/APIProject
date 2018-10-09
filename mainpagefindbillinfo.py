#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:56:17 2018

@author: Aidan
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml?session_year=20172018&house=Assembly&author=All&lawCode=CIV') as homepage:
    soup = BeautifulSoup(homepage.read(), 'html.parser')
 
#Finds relative url    
for link in soup.find_all('a'):
    print(link.get('href'))    
    

#Finds name, subject, author, status
for tr in soup.find_all('td'):
    for tr 
   print(soup.get_text())