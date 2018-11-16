import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root", "")
cursor = db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS SeeFood;"
cursor.execute(sql)
sql = "USE SeeFood;"
cursor.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS `IMAGES` ( 
    `NAME` VARCHAR(191) NOT NULL COLLATE utf8mb4_bin, 
    `PATH` VARCHAR(255) NOT NULL COLLATE utf8mb4_bin,
    `SCORE_1` FLOAT NULL,
    `SCORE_2` FLOAT NULL,
    `HASH` CHAR(32) NULL);'''
cursor.execute(sql)
db.close()
