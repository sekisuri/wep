 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time
from modSQL import InsertProfile
from modSQL import InsertTitle


from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downWEB/mpb_kr_/www.mpb.kr/actor/3.html"
#url = 'http://192.168.0.70/~devuser/mpb/actor/'
url = 'http://www.mpb.kr/actor/'
decimal_regex = r'\d' #정규표현식 숫자만
string_regex = '[A-Z]+' #정규표현식 대문자 알파벳 ..

def av_profile(link):
    profile2 = []
    nameFiled = []
    avProfile={}


    for member_tag in soup.select('.profile tr td'):
        name = member_tag.text
        profile2.append(name)

    sns1 = soup.find('iframe')

    #av 이름
    nameFiled = profile2[1].split('/')
    avProfile['krName'] = nameFiled[0].strip()
    avProfile['enName'] = nameFiled[1].strip()
    avProfile['jaName'] = nameFiled[2].strip()
    #av 이름 저장
    #av 생일
    tmpBirth = "".join(re.findall(decimal_regex,profile2[3]))
    Birth_Year = tmpBirth[0:4]
    Birth_Month = tmpBirth[4:6]
    Birth_Day =  tmpBirth[6:8]
    avProfile['Birthday'] = Birth_Year + "-" + Birth_Month + "-" + Birth_Day
    #av 생일 저장

    #av 사이즈
    tmpCupSize = profile2[5].split('/')
    tmpSize = "".join(re.findall(decimal_regex,profile2[5]))
    #tmpSize = 161342335
    if len(tmpSize) != 9:
        tmpSize = "000000000"
    Height = tmpSize[0:3]
    Bust = tmpSize[3:5]
    Waist = tmpSize[5:7]
    Hip = tmpSize[7:9]
    CupSize = 'C'#"".join(re.findall(string_regex,tmpCupSize[1]))

    if int(Height) < 100 or int(Bust) < 10:
        avProfile['Height'] = 0
        avProfile['Bust'] = 0
        avProfile['Waist'] = 0
        avProfile['Hip'] = 0
        avProfile['CupSize'] = ''
    else:
        avProfile['Height'] = int(Height)
        avProfile['Bust'] = int(Bust)
        avProfile['Waist'] = int(Waist)
        avProfile['Hip'] = int(Hip)
        avProfile['CupSize'] = CupSize

    #av 사이즈 저장

    #av 데뷰일
    Debut = "".join(re.findall(decimal_regex,profile2[7])  )
    DebutYear = Debut[0:4]
    DebutMonth = Debut[4:6]
    DebutDay = Debut[6:8]
    avProfile['Debut'] = DebutYear + "-" + DebutMonth + "-" + DebutDay
    #av 데뷰일 저장

    #av 자기소개 동영상
    if sns1:
        avProfile['SnS1'] = sns1
    else:
        avProfile['SnS1'] = ''

    InsertProfile(avProfile)

#av_profile(url)

def av_title(link):
    tdData = []
    nameFiled = []
    avTitle={}

    content_table = soup.find('table',id='pblist')
    table_body = content_table.find('tbody')
    title_tr = table_body.find_all('tr')
    if title_tr:
        for data in title_tr:
            for td in data:
                tddata = td.text
                tdData.append(tddata)
            avTitle['avId'] = ActorNum
            avTitle['titleName'] = tdData[0]
            avTitle['releaseDate'] = tdData[1].replace("/","-")
            avTitle['koMaker'] = tdData[2]
            age = "".join(re.findall(decimal_regex,tdData[3]))
            if age == '':
                avTitle['titleAge'] = 0
            else:
                avTitle['titleAge'] = int(age)
            avTitle['Mosaic'] = tdData[4]
            InsertTitle(avTitle)
            tdData = []


ActorNum = 1882
MaxActor = 1886
sec = 2
sitelink = url + str(ActorNum)
html = requests.get(sitelink).text
soup = BeautifulSoup(html)
notFound = soup.find("title").text

print("+" *20)
print(sitelink)
print("+" * 20)
av_profile(sitelink)
av_title(sitelink)

"""
while ActorNum < MaxActor:
    #sitelink = url + str(ActorNum) + ".html"
    sitelink = url + str(ActorNum)
    #URL = sitelink
    #res = urllib.request.urlopen(sitelink)
    #html = res.read()
    #soup = BeautifulSoup(html, 'html.parser')
    html = requests.get(sitelink).text
    soup = BeautifulSoup(html)
    notFound = soup.find("title").text
    if notFound.find("404") == 0:
        print("file not found")
        print(sitelink)
        print("-" * 20)
        ActorNum = ActorNum + 1
    else:
        print("+" *20)
        print(sitelink)
        print("+" * 20)
        av_profile(sitelink)
        av_title(sitelink)
        ActorNum = ActorNum + 1
        time.sleep(sec)
"""
