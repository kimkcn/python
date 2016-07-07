#coding: utf-8
from bs4 import BeautifulSoup
import urllib2
import re

response = urllib2.urlopen('http://www.douyutv.com/directory/game/SC')
html = response.read()
soup = BeautifulSoup(html)

room_owner = soup.select('#live-list-contentbox > li > a > div > p > span.dy-name.ellipsis.fl')
room_rate = soup.select('#live-list-contentbox > li > a > div > p > span.dy-num.fr')
room_title = soup.select('#live-list-contentbox > li > a > div > div > h3')
info=[]

for title,owner,num in zip(room_title,room_owner,room_rate):
    tmp=num.get_text()
    try:
        room_rate=int(tmp)
    except ValueError:
        if "." in tmp:
            data=''.join(re.findall('\d+\.?\d+',tmp))
            room_rate = int(float(data)*10000)
        else:
            data=''.join(re.findall('\d+',tmp))
            room_rate = int(data)*10000

    total = [
        title.get_text(),
        owner.get_text(),
        room_rate
    ]
    info.append(total)

for i in info:
    room_rate = i[2]
    if room_rate > 10000:
        print i[0],i[1],i[2]
