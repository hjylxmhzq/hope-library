# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:51:18 2018

@author: hujin
"""
import pymysql
import requests
import time
from findbook import findbooks, findbookinfo
db = pymysql.connect('localhost','root','','test')
cursor = db.cursor()
sql = "SELECT * FROM books;"
cursor.execute(sql)
results = cursor.fetchall()
for book in results:
    try:
        print(book[3])
        r = findbooks(book[3])[0]
        pic = requests.get(r['picurl'])
        if pic.status_code==200:
            open('./covers/'+book[2]+'.jpg','wb').write(pic.content)
    except:
        continue
db.close()