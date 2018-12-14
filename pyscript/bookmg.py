# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:51:18 2018

@author: hujin
"""
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor()
def addbook(category, index, index1, name, location, amount=1):
    sql = "INSERT books(`category`,`index`,`index1`,`name`,`location`,`amount`) VALUES('{}','{}','{}','{}','{}')".format(category,index,index1,name,location,amount)
    cursor.execute(sql)
    db.commit()

def deletebook(index1):
    sql = "DELETE FROM books WHERE `index1`='{}'".format(index1)
    cursor.execute(sql)
    db.commit()

def getbook(name):
    sql = "SELECT * FROM books WHERE `name`='{0}' OR `index`='{0}' OR `index1`='{0}' OR `category`='{0}' OR `location`='{0}'".format(name)
    cursor.execute()
    return cursor.fetchall()

