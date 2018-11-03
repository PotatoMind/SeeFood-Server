from flask import Flask
from flask import request
import random
import string
from werkzeug.utils import secure_filename
import MySQLdb 

# Initialize the Flask application
app = Flask(__name__)
# Initialize the MySQL database connection
db = MySQLdb.connect("localhost", "root", "", "SeeFood")
# Initialize a cursor to perform SQL queries
cursor = db.cursor()

# Main page of the website
@app.route("/")
def index():
    return "Hello World!"

# Upload GET and POST request for images
@app.route('/upload', methods=['GET', 'POST'])
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
        paths = filesFromDB()
        return paths
    db.close()

# Puts files in DB
def fileToDB(file):
    # Get the name from the image that was submitted through POST request
    name = secure_filename(file.filename)
    # Create a string path to the location where we want the image
    ### A unique ID is appended due to duplicate filenames. This needs revised
    path = './files/' + generate_id() + "_" + name
    # SQL query
    sql = "INSERT INTO IMAGES(NAME, PATH) \
        VALUES ('%s', '%s')" % \
        (name, path)
    
    try:
        # This executes the SQL query
        cursor.execute(sql)
        # This commits the changes to the DB
        db.commit()
        # This saves the image to the path location
        file.save(path)
        return "True"
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        # Oh no we fucked up, gotta roll back to a previous DB version
        db.rollback()
        print(e)
        return "False"

# Gets files from DB
def filesFromDB():
    # Also plain old SQL query
    sql = "SELECT * FROM IMAGES"

    try:
        cursor.execute(sql)
        # If we are expecting results, we have to felt them after we query!
        results = cursor.fetchall()
        
        # Loops through every image from query and creates a list of paths
        paths = []
        for image in results:
            #name = image[0]
            paths.append(image[1])
        return paths
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        return "filesFromDB Failed"

# A function to generate 7 random characters
def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))