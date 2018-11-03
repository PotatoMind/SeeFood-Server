# SeeFood-Server
Link to GitHub: https://github.com/aar118/SeeFood-Server

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The ability to run Shell and Python files.

### Installing and Running

1. Open Terminal
2. Clone repository with <code>clone https://github.com/aar118/SeeFood-Server.git</code>
3. Navigate to folder SeeFood-Server
4. Clone SeeFood reposity and follow directions from https://github.com/wsu-wacs/seefood.git
5. Give permissions to server.sh using <code>chmod +x server.sh</code>
6. Run server.sh with <code>./server.sh</code>
7. server.sh will also install packages
8. Make sure to set the username and password for the MySQL when installing

*Note that Debug can be set inside of server.sh*

## Running Example Command:
<code>curl GET 127.0.0.1:5000/upload</code>
<code>curl -X POST -F "the_file=@loaded_fries.png" 127.0.0.1:5000/upload</code>

## Built With

* [Flask](http://flask.pocoo.org/) - Python Web Server
* [Python](https://www.python.org/) - Programming Language for Flask
* [Shell Script](https://www.shellscript.sh/) - Programming Language for Running Server via Terminal
* [SeeFood](https://github.com/wsu-wacs/seefood) - Backend AI
* [MySQLDB](http://mysql-python.sourceforge.net/MySQLdb.html) - MySQL-Python Connection

## Authors

* **Aaron Hammer** - *Developed* - [aar118](https://github.com/aar118)
* **Trevor Konya** - *Developed* - [tkonya](https://github.com/tkonya)
* **Isaiah Winfrey** - *Developed* [iWinfrey](https://github.com/iWinfrey)
* **Madison Yancey** - *Developed* [madison-yancey](https://github.com/madison-yancey)