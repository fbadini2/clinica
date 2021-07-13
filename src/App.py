from flask import Flask, render_template, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
sqlconn = MySQL()


if __name__ == '__main__':
    app.run(debug=True)