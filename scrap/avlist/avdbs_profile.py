 #-*- coding: utf-8 -*-
import requests
import urllib.request
from DB.SQL import InsertName
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
url = 'http://www.avdbs.com/menu/subpage04/profile_view.php?actor_idx=285'	
html = requests.get(url).text
soup = BeautifulSoup(html)
def av_profile():
	avRank = {}
	'''
	for member_tag in soup.select('.av_category_path'):
		#rank = member_tag.find('div',class_='avrank').text
		hentakuName = member_tag.find('li',class_='first_path').find('h1')
		print(hentakuName)
		#avRank['rank_id'] = rank
		#avRank['krName'] = avname
		#avRank['rank_year'] = "2016"
		#avRank['rank_month'] = '10'
		#InsertRank(avRank)
	'''
	
	
	
	av_name = soup.find('div',class_="profile_view_inner")
	av_pic1 = av_name.img
	kr_name = av_name.find('span',class_="inner_name_kr").text
	hentaku_name = kr_name.replace(" ","") #공백제거
	en_name = av_name.find('span',class_="inner_name_en").text
	cn_name = soup.find('span',class_="inner_name_cn").text
	print(hentaku_name)
	print(kr_name)
	print(en_name)
	print(cn_name)
	print(av_pic1)
	
	profile = soup.find('p',class_="profile_bottom_text")
	
	
	pData = []
	
	i = 0
	for rp in profile.find_all('span'):
		pData.append(rp.text)
		#print(pProfile[i])
		i = i + 1
	
	print(pData[0])
	print(pData[1])
	print(pData[2])
	print(pData[4])

av_profile()