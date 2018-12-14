import pymysql
db = pymysql.connect('localhost','root','','test')
cursor = db.cursor()
sql = "SELECT * FROM books;"
cursor.execute(sql)
results = cursor.fetchall()
for book in results:
    print(book[3])