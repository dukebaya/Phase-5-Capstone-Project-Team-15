# Importing relevant packages
import base64
import pandas as pd
import streamlit as st
import numpy as np
import joblib
from joblib import load
import statsmodels
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from altair import Chart

# Load pre-trained model
model = load('model.pkl')
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("image 4.JPG")
# Define function to make predictions using the model
#def predict_activity(input_df):
   # predictions = model.predict(input_df)
    #return 'Yes' if predictions[0] == 1 else 'No'
#def predict_activity(input_df):
   #  predictions = model.predict(input_df)
     #if predictions >= 11.0:
       # return 'Very Likely'
    # elif predictions >= 8.0:
       # return 'High'
     #elif predictions >= 4.0:
      #  return 'Moderate'
    # else:
    #    return 'Less Likely'
#predicted_category = predict_activity(input_df)
#print("Prediction Category:", predicted_category)
def predict_activity(input_df):
    try:
        # Make sure input_df has the correct data types
        numeric_columns = ['year', 'dayofyear', 'dayofweek', 'month', 'quarter', 'hour']
        for column in numeric_columns:
            input_df[column] = pd.to_numeric(input_df[column], errors='coerce').astype('Int64')

        # Predict using the provided model
        predictions = model.predict(input_df)

        # Categorize predictions
        if predictions >= 25.0:
            return 'Very Likely'
        elif predictions >= 17.0:
            return 'High'
        elif predictions >= 9.0:
            return 'Moderate'
        else:
            return 'Less Likely' 
        
    except Exception as e:
        # Handle exceptions and return a default category
        print(f"An error occurred: {e}")
        return 'Unknown'



# Main function for Streamlit web app
def main():
    # Set page title
    st.set_page_config(page_title="ARABUKO SOKOKE", page_icon="Forest Icon.png")
    #st.image('Elephant.jpg', width=400)

    # Display header
    st.title("Illegal Activity Prediction APP")
    st.markdown("<style>h1{color: black;}</style>", unsafe_allow_html=True)

    page_bg_img = f"""
	<style>
	[data-testid="stAppViewContainer"] > .main {{
	background-image: url("data:image/png;base64,{img}");
	background-size: cover;
	background-position: top right;
	background-repeat: no-repeat;
	background-attachment: fixed;
    
	}}
    [data-testid="stWidgetLabel"] p {{
    color: black;
    font-size: 30px;    
    }}
    [data-testid="stMarkdownContainer"] p {{
    color: black;
    font-size: 30px;   
    }}
    [data-testid="stTickBarMax"] {{
    color: black;
    }}

    [data-testid="stHeader"] {{
    background: "rgba(255, 255, 255, 1);
    }}
   [data-testid="stToolbar"] {{
   right: 2rem;
   }}


	</style>
	"""
	

	# header
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # st.sidebar.header("Configuration")
    # Input fields for customer information
    dayofyear = st.number_input('Day of the Year :', min_value=1, max_value=365, value=1)
    hour = st.number_input('Hours:', min_value=0, max_value=23, value=0)
    dayofweek = st.number_input('Day of the week :', min_value=1, max_value=7, value=1)
    quarter = st.slider('Quarter :', min_value=1, max_value=4, value=1)
    month = st.slider('Month :', min_value=1, max_value=12, value=1)
    year= st.number_input('year:', min_value=2018, max_value=2034, value=2018)
      
    # total_day_charge = st.slider('Total day charge:', min_value=0, max_value=60, value=0)
    #total_eve_minutes = st.slider('Total minutes of evening calls:', min_value=0, max_value=400, value=200)
    #total_eve_calls = st.slider('Total number of evening calls:', min_value=0, max_value=200, value=100)
    # total_eve_charge = st.slider('Total evening charge:', min_value=0, max_value=40, value=0)
    #total_night_minutes = st.slider('Total minutes of night calls:', min_value=0, max_value=400, value=200)
    #total_night_calls = st.slider('Total number of night calls:', min_value=0, max_value=200, value=100)
    # total_night_charge = st.slider('Total night charge:', min_value=0, max_value=30, value=0)
    #total_intl_minutes = st.slider('Total minutes of international calls:', min_value=0, max_value=30, value=0)
    #total_intl_calls = st.slider('Total number of international calls:', min_value=0, max_value=30, value=0)
    # total_intl_charge = st.slider('Total international charge:', min_value=0, max_value=20, value=0)
    #customer_service_calls = st.slider('Number of calls to customer service:', min_value=0, max_value=10, value=0)
    #total_charge = st.slider('Total charge:', min_value=0, max_value=100, value=59)
    # total_calls = st.slider('Total number of calls:', min_value=0, max_value=500, value=305)

    # Create input dictionary
    input_dict = {
        'dayofyear': 'Day_of_the_Year',
        'hour': 'Hour',
        'dayofweek': 'Day_of_the_week',
        'quarter': 'Quater',
        'month': 'Month',
        'year': 'year',
        #'international_plan': 1 if international_plan == 'Yes' else 0,
        #'voice_mail_plan': 1 if voice_mail_plan == 'Yes' else 0,
                     
        #'total_night_minutes': total_night_minutes,
        #'total_night_calls': total_night_calls,
        #'total_intl_minutes': total_intl_minutes,
        #'total_intl_calls': total_intl_calls,
        #'customer_service_calls': customer_service_calls,
        #'total_charge': total_charge,
       
    }

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([input_dict])

    #input_df['year'] = input_df['year'].astype(int)
    #input_df['dayofyear'] = input_df['dayofyear'].astype(int)
    #input_df['dayofweek'] = input_df['dayofweek'].astype(int)
    #input_df['month'] = input_df['month'].astype(int)
    #input_df['quarter'] = input_df['quarter'].astype(int)
    #input_df['hour'] = input_df['hour'].astype(int)

    # Convert columns to integers, handling non-numeric values
    numeric_columns = ['year', 'dayofyear', 'dayofweek', 'month', 'quarter', 'hour']
    for column in numeric_columns:
        input_df[column] = pd.to_numeric(input_df[column], errors='coerce').astype('Int64')


    # Make prediction when button is clicked
    if st.button("Predict Logging/Poaching"):
        Illegal_Activity_prediction = predict_activity(input_df)
        st.success(f"Forecast: {Illegal_Activity_prediction}")

# Run the main function if the script is executed
if __name__ == '__main__':
    main()
