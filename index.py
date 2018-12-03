from flask import Flask
from flask import request
from flask import send_file
import random
import string
from werkzeug.utils import secure_filename
import MySQLdb
import zipfile
from io import BytesIO
import time
import datetime
from os.path import basename
import os
from find_food import findFood
import numpy as np
import json
import PIL
from PIL import Image

# Initialize the Flask application
application = Flask(__name__)

# Main page of the website
@application.route("/")
def index():
    return "Hello World!"

# Upload GET and POST request for images
@application.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # If it's a POST request, then we are putting something in the DB
    if request.method == 'POST':
        # This gets the file from the POST request
        f = request.files['the_file']
        # Sends file to DB and saves in images/ folder
        results = fileToDB(f)
	return results
    if request.method == 'GET':
        ### Gets (currently all) paths from DB
        ### Needs to return actual images!
	minRow = request.args.get('minRow')
	maxRow = request.args.get('maxRow')
	images = None
	if minRow is not None and maxRow is not None:
        	return filesFromDB(minRow, maxRow)
	else:
		return filesFromDB()

@application.route('/stats', methods=['GET'])
def stats():
	if request.method == 'GET':
		return str(statsFromDB())
	else:
		return "I'm watching you homie"

# Puts files in DB
def fileToDB(file):
    # Initialize the MySQL database connection
    db = MySQLdb.connect("127.0.0.1", "root", "", "SeeFood")
    # Initialize a cursor to perform SQL queries
    cursor = db.cursor()
    # Get the name from the image that was submitted through POST request
    # Also, some other variables for later
    name, ext = os.path.splitext(secure_filename(file.filename))
    if ext != ".png" and ext != ".jpg" and ext != ".jpeg":
	return "Not an image!"
    path = 'files/' + name + ext
    scores = None
    conf_score = None

    # If the file doesn't already exist in the folder (meaning it's from the image gallery)
    if not os.path.exists(path):
        # Create a string path to the location where we want the image
        # A unique ID is appended due to duplicate filenames. This needs revised
        name = generate_id()
        path = 'files/' + name + ext
        while os.path.exists(path):
            path = 'files/' + generate_id()
        try:
	    file.save(path)
	    basewidth = 300
	    image = Image.open(path).convert('RGB')
	    wpercent = (basewidth / float(image.size[0]))
	    hsize = int((float(image.size[1]) * float(wpercent)))
	    image = image.resize((basewidth, hsize), Image.BILINEAR)
	    image.save(path, "JPEG")
        except Exception as e:
            db.close()
            cursor.close()
	    print(e)
            return "Couldn't save for some dang reason"
        scores = findFood(path)
        conf_score = abs(scores[0,0] - scores[0,1])

        # SQL query
        sql = "INSERT INTO IMAGES(NAME, EXT, SCORE_1, SCORE_2) \
            VALUES ('%s', '%s', '%f', '%f')" % \
            (name, ext, scores[0,0], scores[0,1])

        try:
            # This executes the SQL query
            cursor.execute(sql)
            # This commits the changes to the DB
            db.commit()
            # This saves the image to the path location
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            # Oh no we fucked up, gotta roll back to a previous DB version
            db.rollback()
            db.close()
            cursor.close()
            print(e)
            return "IT BROKE YO"
        else:
            scores = findFood(path)
            conf_score = abs(scores[0,0] - scores[0,1])

        db.close()
        cursor.close()
        # if np.argmax = 0; then the first class_score was higher, e.g., the model sees food.
        # if np.argmax = 1; then the second class_score was higher, e.g., the model does not see food.
        if np.argmax(scores) == 1:
            if conf_score < 1:
                return "Low No"
            elif conf_score < 2:
                return "Moderate No"
            else:
                return "High No"
        else:
            if conf_score < 1:
                return "Low Yes"
            elif conf_score < 2:
                return "Moderate Yes"
            else:
                return "High Yes"

def statsFromDB():
    # Initialize the MySQL database connection
    db = MySQLdb.connect("127.0.0.1", "root", "", "SeeFood")
    # Initialize a cursor to perform SQL queries
    cursor = db.cursor()

     # Also plain old SQL query
    sql = "SELECT * FROM IMAGES \
        WHERE DATE_FORMAT(CREATED_AT, '%%Y-%%m-%%d') = DATE_FORMAT(NOW(), '%%Y-%%m-%%d')"

    sql2 = "SELECT * FROM IMAGES"

    try:
        cursor.execute(sql)
        # If we are expecting results, we have to felt them after we query!
        results = cursor.fetchall()
	cursor.execute(sql2)
	results2 = cursor.fetchall()
	if results is None or results2 is None:
        	db.close()
        	cursor.close()
		return "No results"
        # Loops through every image from query and creates a list of paths
        db.close()
        cursor.close()

	lowNoTodayCount = 0
	modNoTodayCount = 0
	highNoTodayCount = 0
	lowYesTodayCount = 0
	modYesTodayCount = 0
	highYesTodayCount = 0
	for image in results:
	    scores = [image[3], image[4]]
            conf_score = abs(scores[0] - scores[1])
            score = "None"
            if np.argmax(scores) == 1:
                if conf_score < 1:
                    lowNoTodayCount += 1
                elif conf_score < 2:
                    modNoTodayCount += 1
                else:
                    highNoTodayCount += 1
            else:
                if conf_score < 1:
		    lowYesTodayCount += 1
                elif conf_score < 2:
                    modYesTodayCount += 1
                else:
                    highYesTodayCount += 1

	lowNoAllCount = 0
	modNoAllCount = 0
	highNoAllCount = 0
	lowYesAllCount = 0
	modYesAllCount = 0
	highYesAllCount = 0
	for image in results2:
	    scores = [image[3], image[4]]
            conf_score = abs(scores[0] - scores[1])
            if np.argmax(scores) == 1:
                if conf_score < 1:
                    lowNoAllCount += 1
                elif conf_score < 2:
                    modNoAllCount += 1
                else:
                    highNoAllCount += 1
            else:
                if conf_score < 1:
		    lowYesAllCount += 1
                elif conf_score < 2:
                    modYesAllCount += 1
                else:
                    highYesAllCount += 1

        return json.dumps({
		"numToday": len(results),
		"numAllTime": len(results2), 
		"lowNoToday": lowNoTodayCount,
		"modNoToday": modNoTodayCount,
	        "highNoToday": highNoTodayCount,
	        "lowYesToday": lowYesTodayCount,
		"modYesToday": modYesTodayCount,
		"highYesToday": highYesTodayCount, 
		"lowNoAll": lowNoAllCount,
		"modNoAll": modNoAllCount,
	        "highNoAll": highNoAllCount,
	        "lowYesAll": lowYesAllCount,
		"modYesAll": modYesAllCount,
		"highYesAll": highYesAllCount,
		"numYesAllTime": lowYesAllCount + modYesAllCount + highYesAllCount,
		"numNoAllTime": lowNoAllCount + modNoAllCount + highNoAllCount
		})
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        db.close()
        cursor.close()
        return "filesFromDB Failed"

def filesFromDB(minRow = '0', maxRow = '50000'):
    # Initialize the MySQL database connection
    db = MySQLdb.connect("127.0.0.1", "root", "", "SeeFood")
    # Initialize a cursor to perform SQL queries
    cursor = db.cursor()

    # Also plain old SQL query
    sql = "SELECT NAME, EXT, SCORE_1, SCORE_2 FROM IMAGES \
	 LIMIT %s,%s" % \
	(minRow, maxRow)

    try:
        cursor.execute(sql)
        # If we are expecting results, we have to felt them after we query!
        results = cursor.fetchall()
	if len(results) == 0:
        	db.close()
       		cursor.close()
		return "No results"
        # Loops through every image from query and creates a list of paths
        images = []

        for image in results:
            data = {}
	    data['path'] = 'http://3.16.73.99/files/' + image[0] + image[1]
	    scores = [image[2], image[3]]
            conf_score = abs(scores[0] - scores[1])
            score = "None"
            if np.argmax(scores) == 1:
                if conf_score < 1:
                    score = "Low No"
                elif conf_score < 2:
                    score = "Moderate No"
                else:
                    score = "High No"
            else:
                if conf_score < 1:
                    score = "Low Yes"
                elif conf_score < 2:
                    score = "Moderate Yes"
                else:
                    score = "High Yes"
	    data['score'] = score
            images.append(data)

        db.close()
        cursor.close()
        return str(json.dumps(images))
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        db.close()
        cursor.close()
        return "filesFromDB Failed"


# A function to generate 7 random characters
def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    application.run(host='0.0.0.0')
