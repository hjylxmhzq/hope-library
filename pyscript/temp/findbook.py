# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:51:18 2018

@author: hujin
"""

import requests
from bs4 import BeautifulSoup

def findbook(name):
    url = 'https://www.douban.com/search?cat=1001&q='+name
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    resultlist = soup.select('.result')
    all = []
    for result in resultlist:
        try:
            picurl = result.contents[1].a.img['src']
            bookname = result.contents[1].a['title']
            bookurl = result.contents[1].a['href']
            description= result.contents[3].p.get_text()
            all.append({'picurl':picurl,'bookname':bookname,'bookurl':bookurl,'description':description})
        except:
            continue
    return all
a = findbook('态度')

def findbookinfo(bookurl):
    response = requests.get(bookurl)
    soup = BeautifulSoup(response.content,'html.parser')
    info = soup.select('#info')
    text = info[0].text.replace(' ','').replace('\n\n','\n').replace('\n\n','\n').replace('\n\n','\n')
    return text
    