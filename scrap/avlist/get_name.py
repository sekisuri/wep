 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time
from getNameSQL import InsertName


from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW

url = 'https://hentaku.net/list.php?sort=&page=1'
html = requests.get(url).text
soup = BeautifulSoup(html)
count = 0
for member_tag in soup.select('.list a'):
    count = count + 1
    link = member_tag['href']
    #print(link.split('/')[2])
    InsertName(link.split('/')[2])
    
