# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 01:36:59 2018

@author: hujin
"""

from flask import Flask, render_template, request, jsonify
from bookmg import *
app = Flask(__name__)


class nav:
    def __init__(self, href, text):
      self.href = href
      self.text = text

nav = [nav('/category/booksofpr','编程类'), nav('/category/booksofds','设计类'),nav('/category/booksofnm','网管类'),nav('/category/booksofhm','人文类'),nav('/category/booksofle','博雅教育'),nav('/category/booksofpg','摄影类')]

@app.route('/')
def index(category=None):
    return render_template('index.html', navigation=nav)

@app.route('/category/<category>')
def category(category=None):
    displaybooks = []
    print(category)
    try:
        page = int(request.args.get('page'))
    except:
        page = 0
    if category == 'booksofpr':
        books = getbook('编程类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofds':
        books = getbook('设计类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofpg':
        books = getbook('摄影类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofnm':
        books = getbook('网管类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofhm':
        books = getbook('人文类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofsw':
        books = getbook('软件教程类')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    if category == 'booksofle':
        books = getbook('博雅教育')
        batch = 0
        for book in books[page*50:]:
            if batch > 50:
                break
            batch+=1
            displaybooks.append({'index1':book[2],'name':book[3]})
    return render_template('index.html', navigation=nav, books=displaybooks)

@app.route('/search')
def search():
    keyword = ''
    names = []
    try:
        keyword = request.args.get('keyword')
    except:
        keyword = ''
    books = getsomebooks(keyword)
    result = books[:10]
    for name in result:
        names.append(name[3])
    return jsonify(names)

@app.route('/searchpage')
def searchpage():
    keyword = ''
    displaybooks = []
    try:
        keyword = request.args.get('keyword')
    except:
        keyword = ''
    books = getsomebooks(keyword)
    for book in books:
        displaybooks.append({'index1':book[2],'name':book[3]})
    return render_template('searchpage.html', navigation=nav, books=displaybooks)

@app.route('/book/<index1>')
def bookpage(index1=None):
    book = getabook(index1)
    book = book[0]
    status = ''
    if book[9] == 0:
        status = '未借出'
    else:
        status = '已借出'
    book = {'status': status, 'name': book[3], 'location': book[6], 'description': book[4], 'index1': book[2], 'bookurl': book[5]}
    return render_template('book.html', book=book)

@app.route('/recommend')
def recommendindex():
    return render_template('recommendindex.html')




if __name__ == '__main__':
    app.run()