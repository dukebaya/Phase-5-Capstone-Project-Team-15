
from flask import Flask,request,render_template, jsonify
import numpy as np
import pandas as pd
import joblib
import base64
import statsmodels
from sklearn.preprocessing import StandardScaler
from joblib import load

application=Flask(__name__)

app=application

# Load pre-trained model
model = joblib.load('trained_model.pkl')

# Define function to make predictions using the model
def predict(features):
    # Make prediction using the loaded model
    prediction = model.predict([features])[0]
    return prediction

@app.route('/login')
def login():
    # Render login page
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('arabuko.html')

#@app.route('/map')
#def map():
    # Render map page
   # return render_template('map.html')



# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict_api():
    # Get data from request
    data = request.json
    
    # Extract features from the request data
    features = data.get('features', [])
    
    # Make prediction
    prediction = predict(features)
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)


