 #-*- coding: utf-8 -*-
import requests
import urllib.request
from DB.SQL import InsertName
from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW

for i in range(1,2721): 
    
    url = 'http://www.avdbs.com/menu/subpage04/profile_view.php?actor_idx=' + str(i)
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    print(url)
    count = 0
    for member_tag in soup.select('.list a'):
        count = count + 1
        link = member_tag['href']
        #print(link.split('/')[2])
        InsertName(link.split('/')[2])
    