import flask
from flask import Flask,jsonify,request
import json
import pickle
import numpy as np
from data_input import data_in

app = Flask(__name__)

#loading the model
def load_model():
    file_name = 'ds_salary_model_file.p'
    with open(file_name,'rb') as m:
        data = pickle.load(m)
        model = data['model']
    return model

@app.route('/',methods=['GET'])
def predict():

    x = np.array(data_in).reshape(1,-1)
    #loading the model
    model = load_model() #the function we made above
    pred = model.predict(x)[0]
    response = json.dumps({'Predicted Salary for the data is:':pred})
    return response

if __name__ == '__main__':
    app.run(host="localhost", port=8000,debug=True)
