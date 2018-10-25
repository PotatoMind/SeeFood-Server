from flask import Flask
from flask import request
import random
import string
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/test")
def test():
    return "Test!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('./files/' + generate_id() + "_" + secure_filename(f.filename))
        return "Success"
    if request.method == 'GET':
        return "You'll get your files eventually"


def fileToDB(file):
	return file

def fileFromDB():
	file = open("Test")
	return file

def generate_id(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))