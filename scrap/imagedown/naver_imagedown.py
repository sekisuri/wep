# -*- coding: utf-8 -*- 

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

import urllib.request

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = '황민현'#input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgUrl = i['data-source']
    chimg = imgUrl.replace('&type=b400','')
    print(chimg)
    urllib.request.urlretrieve(imgUrl,'./16/' + plusUrl + str(n)+'.jpg')
    n += 1
print('다운로드 완료')