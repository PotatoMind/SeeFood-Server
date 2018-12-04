# SeeFood-Server

Link to GitHub: https://github.com/aar118/SeeFood-Server<br/>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.<br/>

### Prerequisites

The ability to run Shell and Python files.<br/>

### Installing and Running

1. Open Terminal<br/>
2. Clone repository with <code>clone https://github.com/aar118/SeeFood-Server.git</code><br/>
3. Navigate to folder SeeFood-Server<br/>
4. Follow directions from https://github.com/wsu-wacs/seefood.git<br/>
5. Give permissions to server.sh using <code>chmod +x server.sh</code><br/>
6. Run server.sh with <code>./server.sh</code><br/>
7. server.sh will also install packages<br/>
8. Make sure to set the username and password for the MySQL when installing<br/>

*Note that Debug can be set inside of server.sh*<br/>
*Also note that a development server shouldn't be used for production*

## Running Example Command:

<code>curl GET 127.0.0.1:5000/upload</code><br/>
<code>curl -X POST -F "the_file=@loaded_fries.png" 127.0.0.1:5000/upload</code><br/>

## Built With

* [Flask](http://flask.pocoo.org/) - Python Web Server<br/>
* [Python](https://www.python.org/) - Programming Language for Flask<br/>
* [Shell Script](https://www.shellscript.sh/) - Programming Language for Running Server via Terminal<br/>
* [SeeFood](https://github.com/wsu-wacs/seefood) - Backend AI<br/>
* [MySQLDB](http://mysql-python.sourceforge.net/MySQLdb.html) - MySQL-Python Connection<br/>

## Authors

* **Aaron Hammer** - *Developed* - [aar118](https://github.com/aar118)<br/>
* **Trevor Konya** - *Developed* - [tkonya](https://github.com/tkonya)<br/>
* **Isaiah Winfrey** - *Developed* [iWinfrey](https://github.com/iWinfrey)<br/>
* **Madison Yancey** - *Developed* [madison-yancey](https://github.com/madison-yancey)