source activate py27
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install mysql-server
pip install MySQL-python
pip install Flask
python mysql.py
export FLASK_APP=index.py
export FLASK_DEBUG=0
flask run --host=0.0.0.0
