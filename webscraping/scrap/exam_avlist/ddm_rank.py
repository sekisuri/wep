 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time

from ddm_rankSQL import InsertRank



from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downWEB/mpb_kr_/www.mpb.kr/actor/3.html"
#url = 'http://192.168.0.70/~devuser/mpb/actor/'
url = 'https://hentaku.net/rank/'
html = requests.get(url).text
soup = BeautifulSoup(html)
decimal_regex = r'\d' #정규표현식 숫자만
string_regex = '[A-Z]+' #정규표현식 대문자 알파벳 ..

def av_profile():
    avRank = {}


    for member_tag in soup.select('.avstar_warp'):
        #rank = member_tag.find('div',class_='avrank').text
        avname = member_tag.find('div',class_='avstar_info_b').text
        print(avname)
        #avRank['rank_id'] = rank
        #avRank['krName'] = avname
        #avRank['rank_year'] = "2016"
        #avRank['rank_month'] = '10'
        #InsertRank(avRank)

av_profile()
