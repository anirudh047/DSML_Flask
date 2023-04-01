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

#defining the endpoint which will make the prediction
@app.route("/predict", methods=['POST'])
def prediction():
    """ Returns loan application status using ML model
    """ 
    loan_req = request.get_json()
    print(loan_req) 
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else: 
        Credit_History = 1
    
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']/1000 #loan amt is divided by 1000 as the model expects in multiples of 1000 

    input_data=[[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]]

    prediction = clf.predict(input_data)

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {"loan_approval_status: ": pred}


@app.route("/get_params", methods=["Get"] )
def get_params ():
    parameters = {
                "Gender":"Male",
                "Married": "Unmarried",
                "ApplicantIncome": 50000,
                "Credit_History": "Cleared Debts",
                "LoanAmount": 500000
        }

    return parameters

#Use Postman to verify the API enpoint by oassing a POST request with the JSON dict in Body 