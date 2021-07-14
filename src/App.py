from flask import Flask, render_template, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
sqlconn = MySQL()

# conexion a mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#171Nolaadi'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


if __name__ == '__main__':
    app.run(debug=True)