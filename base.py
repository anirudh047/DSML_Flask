from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/ping")
def hello_ping():
    return "<h1>Pinging the new endpoint.....</h1>"

@app.route("/user/<username>")
def hello_variable(username):
    return f'User: {escape(username)}'

#To run the application use below cmd line (where 'base' is the file name)
# flask --app base run