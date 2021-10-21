import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage=1&rowPerPage=300'

html = requests.get(url).text
soup = BeautifulSoup(html)
#soup = BeautifulSoup(html, from_encoding='utf-8')
for member_tag in soup.select('.memberna_list dl dt a'):
    name = member_tag.text
    link = member_tag['href']
    print("link : {}".format(link))

    matched = re.search(r'\d+',link)
    print("matched : {}".format(matched))
    if matched:
        member_id = matched.group(0)
        print("member id : {}".format(member_id))
    else:
        member_id = None
    #print(unicode(name),link)
    #print str(name.head).decode('utf8')
    strtest = name + ': ' + member_id
    print(strtest)
    print(member_id)
    #print str(bs.head).decode('utf8')
