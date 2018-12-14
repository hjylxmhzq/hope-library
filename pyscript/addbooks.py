#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import *
import pymysql
import csv
# 创建数据库引擎,echo为True,会打印所有的sql语句
db = pymysql.connect("localhost","root","","test" )
f = open('books.csv','r',encoding='utf8')
data = list(csv.reader(f))
f.close()
# 创建一个connection，这里的使用方式与python自带的sqlite的使用方式类似
cursor = db.cursor()
for i in data:
    sql = "INSERT books(`category`, `index`, `index1`, `name`, `location`) VALUES('{}','{}','{}','{}','{}')".format(i[0],i[1],i[2],i[3],i[4])
    cursor.execute(sql)
    db.commit()
db.close()
