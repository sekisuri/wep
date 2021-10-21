 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time
from ddm_rankSQL import InsertRank




from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downWEB/mpb_kr_/www.mpb.kr/actor/3.html"
#url = 'http://192.168.0.70/~devuser/mpb/actor/'
url = 'http://www.mpb.kr/dmmrank'
html = requests.get(url).text
soup = BeautifulSoup(html)
decimal_regex = r'\d' #정규표현식 숫자만
string_regex = '[A-Z]+' #정규표현식 대문자 알파벳 ..

def av_profile():
    avRank = {}


    for member_tag in soup.select('.mactorul'):
        avname = member_tag.find('a',class_='mactor').text
        tmprank = member_tag.find('span',class_='ico_job').text
        avrank = "".join(re.findall(decimal_regex,tmprank))

        avRank['krName'] = avname
        avRank['rank_id'] = avrank
        avRank['rank_year'] = "2016"
        avRank['rank_month'] = '10'
        InsertRank(avRank)
        #print(avname)
        #print(avrank)


av_profile()
