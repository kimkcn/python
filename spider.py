#coding: utf-8
from bs4 import BeautifulSoup
import urllib2
import re

response = urllib2.urlopen('http://www.douyutv.com/directory/game/SC')
html = response.read()
soup = BeautifulSoup(html)

room_owner = soup.select('#live-list-contentbox > li > a > div > p > span.dy-name.ellipsis.fl')
room_num = soup.select('#live-list-contentbox > li > a > div > p > span.dy-num.fr')
room_title = soup.select('#live-list-contentbox > li > a > div > div > h3')
info=[]

for title,owner,num in zip(room_title,room_owner,room_num):
    tmp=num.get_text()
    try:
        room_num=int(tmp)
    except ValueError:
        if "." in tmp:
            data=''.join(re.findall('\d+\.?\d+',tmp))
            room_num = int(float(data)*10000)
        else:
            data=''.join(re.findall('\d+',tmp))
            room_num = int(data)*10000

    total = [
        title.get_text(),
        owner.get_text(),
        room_num
    ]
    info.append(total)

for i in info:
    room_num = i[2]
    if room_num > 10000:
        print i[0],i[1],i[2]
