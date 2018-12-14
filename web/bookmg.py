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
    cursor.execute(sql)
    return cursor.fetchall()

def getabook(name):
    sql = "SELECT * FROM books WHERE `index1`='{0}'".format(name)
    cursor.execute(sql)
    return cursor.fetchall()

def getsomebooks(name):
    sql = "SELECT * FROM books WHERE `name` LIKE '%{0}%' OR `index` LIKE '%{0}%' OR `index1` LIKE '%{0}%' OR `category` LIKE '%{0}%' OR `location` LIKE '%{0}%' LIMIT 10 ".format(name)
    cursor.execute(sql)
    return cursor.fetchall()
