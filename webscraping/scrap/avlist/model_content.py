 #-*- coding: utf-8 -*-
import requests
import urllib.request
from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW

    
url = 'https://hentaku.net/star/%ED%83%80%EC%B9%B4%ED%95%98%EC%8B%9C%EC%87%BC%EC%BD%94'
html = requests.get(url).text
#html = urlopen(url).read()
soup = BeautifulSoup(html)
avname  = soup.h2.a.string
split_name = avname.split('/')
kName = split_name[0].strip()
eName = split_name[1].strip()
jName = split_name[2].replace("품번","").strip()

print(kName)
print(eName)
print(jName)

for member_tag in soup.select('.avstar_info_b'):
	tmp = member_tag
profile = tmp.split('/')
print(profile)

