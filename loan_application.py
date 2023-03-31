import pickle
import requests
from flask import Flask, request


app = Flask(__name__)

#import model
model = open('./classifier.pkl', 'rb')
clf = pickle.load(model)


@app.route("/ping")
def hello_ping():
    return "<h1>Pinging the model file</h1>"

#To run the application use below cmd line (where 'loan_application' is the file name)
# flask --app loan_application run