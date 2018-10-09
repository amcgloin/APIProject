#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:56:17 2018

@author: Aidan
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

with urlopen('https://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml?session_year=20172018&house=Senate&author=All&lawCode=PROB') as homepage:
    soup = BeautifulSoup(homepage.read(), 'html.parser')
 
#Finds relative url    
for link in soup.find_all('a'):
     print(urljoin('https://leginfo.legislature.ca.gov', link.get('href')))