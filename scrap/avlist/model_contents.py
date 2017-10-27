 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time


from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW

    
url = 'https://hentaku.net/star/%ED%83%80%EC%B9%B4%ED%95%98%EC%8B%9C%EC%87%BC%EC%BD%94'
html = requests.get(url).text
soup = BeautifulSoup(html)
# for member_tag in soup.select('.avstar_info_b'):
for member_tag in soup.select('.avstar_warp'):
    #rank = member_tag.find('div',class_='avrank').text
    new_tag = member_tag.new_tag("b")
    new_Tag.string = "/"
    avname = member_tag.find('div',class_='avstar_info_b')
    avname.br.replace_with(new_tag)
    print(avname)
    #avRank['rank_id'] = rank
    #avRank['krName'] = avname
    #avRank['rank_year'] = "2016"
    #avRank['rank_month'] = '10'
    #InsertRank(avRank)
