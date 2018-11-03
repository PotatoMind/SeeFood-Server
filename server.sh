source activate py27
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install mysql-server
pip install MySQL-python
pip install Flask
python mysql.py
export FLASK_APP=index.py
export FLASK_DEBUG=1
python -m flask run