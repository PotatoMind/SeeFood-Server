import os
import shutil
import MySQLdb

folderPath = "files"
for f in os.listdir(folderPath):
	path = os.path.join(folderPath, f)
	try:
		if os.path.isfile(path):
			os.unlink(path)
	except Exception as e:
		print(e)

db = MySQLdb.connect("127.0.0.1", "root", "")
cursor = db.cursor()

sql = "DROP DATABASE SeeFood"
try:
	cursor.execute(sql)
	db.commit()
except (MySQLdb.Error, MySQLdb.Warning) as e:
	db.rollback()
	print(e)

db.close()
cursor.close()
