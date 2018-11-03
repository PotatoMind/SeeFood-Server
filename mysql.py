import MySQLdb

db = MySQLdb.connect("localhost", "root", "")
cursor = db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS SeeFood;"
cursor.execute(sql)
sql = "USE SeeFood;"
cursor.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS IMAGES ( 
    NAME VARCHAR(255) NOT NULL, 
    PATH VARCHAR(255) NOT NULL );'''
cursor.execute(sql)
db.close()