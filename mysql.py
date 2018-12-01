import MySQLdb

db = MySQLdb.connect("127.0.0.1", "root", "")
cursor = db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS SeeFood;"
cursor.execute(sql)
sql = "USE SeeFood;"
cursor.execute(sql)
sql = '''CREATE TABLE IF NOT EXISTS `IMAGES` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `NAME` VARCHAR(191) NOT NULL COLLATE utf8mb4_bin,
    `EXT` VARCHAR(191) NOT NULL COLLATE utf8mb4_bin,
    `SCORE_1` FLOAT NULL,
    `SCORE_2` FLOAT NULL,
    `CREATED_AT` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID));'''
cursor.execute(sql)
db.close()
