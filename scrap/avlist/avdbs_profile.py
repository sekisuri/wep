 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
#from DB.SQL import InsertName
from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW
'''
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
    

'''
decimal_regex = r'\d' #정규표현식 숫자만
string_regex = '[A-Z]+' #정규표현식 대문자 알파벳 ..
url = 'http://www.avdbs.com/menu/subpage04/profile_view.php?actor_idx=285'	
html = requests.get(url).text
soup = BeautifulSoup(html)
def av_profile():
	avRank = {}

	
	av_name = soup.find('div',class_="profile_view_inner")
	main_pic = av_name.img.get('src') # img 태그의 src 속성을 가져온다.
	kr_name = av_name.find('span',class_="inner_name_kr").text
	hentaku_name = kr_name.replace(" ","") #공백제거
	en_name = av_name.find('span',class_="inner_name_en").text
	cn_name = soup.find('span',class_="inner_name_cn").text
	print(hentaku_name) #hentaku 에서 인식될 한국어이름
	print(kr_name) # 한국어 이름
	print(en_name) # 영어 이름
	print(cn_name) # 일본 이름
	print(main_pic) # 사진
	
	profile = soup.find('p',class_="profile_bottom_text")
	pData = []
	
	i = 0
	for rp in profile.find_all('span'): #프로필 데이터를 가져오기 위해 반복문
		pData.append(rp.text)
		#print(pProfile[i])
		i = i + 1
	
	
	pbirth = "" . join(re.findall(decimal_regex,pData[0])) #생일
	pheight = "" . join(re.findall(decimal_regex,pData[1])) #키
	psize = "" . join(re.findall(decimal_regex,pData[2])) #신체사이즈
	pcupsize = "" . join(re.findall(string_regex,pData[3]))#가슴 컵
	pdebut = "" . join(re.findall(decimal_regex,pData[4])) #데뷰일

	print(pbirth)
	print(pheight)
	print(psize)
	print(pcupsize)
	print(pdebut)
	
	# 기타 이미지를 가져온다.
	otherpic = []
	j = 0
	apic = soup.find('div',class_="other_photo_list")
	for ppic in apic.find_all('li'):
		if 'go_popup' in ppic.a.get('onclick'): # 끝 부분에 광고 주소가 들어가기 때문에 'go_popup'를 중심으로 걸려낸다.
			otherpic.append(ppic.a.get('onclick').replace("go_popup('","").replace("');",""))

			print(otherpic[j])
		j = j + 1
	
	#avpic1 = otherpic[0].replace("');")
	
	
av_profile()