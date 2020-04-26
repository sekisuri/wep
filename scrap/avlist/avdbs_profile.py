 #-*- coding: utf-8 -*-
import re
import requests
import urllib.request
import time
from DB.SQL import InsertProfile
from bs4 import BeautifulSoup
#url = "http://192.168.0.7/downW
decimal_regex = r'\d' #정규표현식 숫자만
string_regex = '[A-Z]+' #정규표현식 대문자 알파벳 ..

def av_profile(index):
	
	url = 'http://www.avdbs.com/menu/subpage04/profile_view.php?actor_idx=' + str(index)
	html = requests.get(url).text
	soup = BeautifulSoup(html)
	insertDB = {} #디비에 넣기위해	
	otherpic = [] # 기타 이미지를 가져온다.

# 에러를 피하기 위해 변수에 초기값 초기값을 넣는다. 
	av_name = "?"
	main_pic = "http://addingfriends.net/image/blank.jpg"
	kr_name = "?"
	hentaku_name = kr_name.replace(" ","") #공백제거
	en_name = "?"
	cn_name = "?"
	pbirth = "00000000"
	pheight = "000"
	psize = "000000"
	pcupsize = "?"
	pdebut = "0000"
	for i in range(0,5):
		otherpic.append("http://addingfriends.net/image/blank.jpg")
# 변수 초기화 끝
	av_name = soup.find('div',class_="profile_view_inner")
	main_pic = av_name.img.get('src') # img 태그의 src 속성을 가져온다.
	kr_name = av_name.find('span',class_="inner_name_kr").text
	hentaku_name = kr_name.replace(" ","") #공백제거
	en_name = av_name.find('span',class_="inner_name_en").text
	cn_name = soup.find('span',class_="inner_name_cn").text
	
	insertDB['avdb'] = index
	
	insertDB['hentaku'] = hentaku_name
	insertDB['krname'] = kr_name
	insertDB['enname'] = en_name
	insertDB['janame'] = cn_name
	
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

	
	insertDB['height'] = pheight
	insertDB['size'] = psize
	insertDB['bustcup'] = pcupsize
	insertDB['birthday'] = pbirth
	insertDB['debut'] = pdebut
	
	
	
	j = 0
	apic = soup.find('div',class_="other_photo_list")
	for ppic in apic.find_all('li'):
		if 'go_popup' in ppic.a.get('onclick'): # 끝 부분에 광고 주소가 들어가기 때문에 'go_popup'를 중심으로 걸려낸다.
			otherpic.insert(j, ppic.a.get('onclick').replace("go_popup('","").replace("');",""))

			#print(otherpic[j])
		j = j + 1
	
	#avpic1 = otherpic[0].replace("');")
	''''''
	insertDB['mainpic'] = main_pic
	insertDB['pic1'] = otherpic[0]
	insertDB['pic2'] = otherpic[1]
	insertDB['pic3'] = otherpic[2]
	insertDB['pic4'] = otherpic[3]
	insertDB['pic5'] = otherpic[4]
	InsertProfile(insertDB)
	
	'''
	insertDB['avdb'] = 285
	insertDB['mainpic'] = main_pic
	insertDB['hentaku'] = hentaku_name
	insertDB['krname'] = kr_name
	insertDB['enname'] = en_name
	insertDB['janame'] = cn_name
	insertDB['height'] = pheight
	insertDB['bust'] = psize[0:2]
	insertDB['waist'] = psize[2:4]
	insertDB['hip'] = psize[4:6]
	insertDB['bustcup'] = pcupsize
	insertDB['birthday'] = pbirth
	insertDB['debut'] = pdebut
	insertDB['pic1'] = otherpic[0]
	insertDB['pic2'] = otherpic[1]
	insertDB['pic3'] = otherpic[2]
	insertDB['pic4'] = otherpic[3]
	insertDB['pic5'] = otherpic[4]
	print(insertDB['avdb'])
	print(insertDB['mainpic'])
	print(insertDB['hentaku'])
	print(insertDB['krname'])
	print(insertDB['enname'])
	print(insertDB['janame'])
	print(insertDB['height'])
	print(insertDB['size'])
	print(insertDB['bustcup'])
	print(insertDB['birthday'])
	print(insertDB['debut'])
	print(insertDB['pic1'])
	print(insertDB['pic2'])
	print(insertDB['pic3'])
	print(insertDB['pic4'])
	print(insertDB['pic5'])
	'''

for i in range(1,2721): 
	av_profile(i)
	print(i)
	time.sleep(3) # 3초간 쉰다.