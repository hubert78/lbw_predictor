import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
#from io import BytesIO
#import os




# Function to download the file from a URL
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return BytesIO(response.content)
    



def diabetes_predictor():
  st.subheader('Diabetes Prediction')
 
  with st.expander('Patient socio-demographic details'):
    col1, col2 = st.columns(2)
    with col1:
      num_pregnancy = st.number_input('Number of Pregnancies', min_value=0, max_value=50, value=0)
      
    with col2:
      age = st.number_input('Age (years)', min_value=10, max_value=100, value=30)
    
    col1, col2 = st.columns(2)
    with col1:
      glucose = st.number_input('Glucose level (mg/dL)', min_value=40.00, max_value=250.00, value=120.00)
      
    with col2:
      insulin = st.number_input('Insulin (IU/mL)', min_value=0, max_value=900, value=80)
  
    col1, col2 = st.columns(2)
    with col1:
      bmi = st.number_input('BMI (kg/m^2)', min_value=15.00, max_value=70.00, value=30.00)
      
    with col2:
      blood_pressure = st.number_input('Blood Pressure (mmHg)', min_value=20, max_value=140, value=70)

    col1, col2 = st.columns(2)
    with col1:
      skin_thickness = st.number_input('Skin Thickness (mm)', min_value=7, max_value=150, value=30)
      
    with col2:
      dpf = st.number_input('Diabetes Pedigree Function (mmHg)', min_value=0.10, max_value=3.00, value=0.45)  
  
  
  
  df = pd.DataFrame()
  
  if st.button('Check prediction'):
      data_list = [
          num_pregnancy, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age
      ]
      
      col_names = [
          'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'
      ]
  
      # Wrap data_list in another list to make it a 2D list
      df = pd.DataFrame([data_list], columns=col_names)    
    
      # Feature Engineering
      # Let's create bins for our Pregnancies categorization.
      bins = [0, 1, 3, 20]
      labels = ['No Pregnancy', '1-2 Pregnancies', 'More than 2 Pregnancies']
      df['CAT_Pregnancies'] = pd.cut(df['Pregnancies'], bins=bins, labels=labels, right=False)
      
      # Let's create bins for our glucose categorization.
      bins = [0, 100, 125, 400]
      labels = ['Normal', 'Pre-diabetic', 'Diabetic']
      df['CAT_Glucose'] = pd.cut(df['Glucose'], bins=bins, labels=labels, right=False)
      
      # Let's create bins for our blood pressure categorization.
      # This assumes that the data presented is Diastolic Blood pressure readings.
      bins = [0, 80, 120, 200]
      labels = ['Normal', 'Pre-hypertension', 'Hypertensive Crises']
      df['CAT_BloodPressure'] = pd.cut(df['BloodPressure'], bins=bins, labels=labels, right=False)

      # Let's create bins for our insulin categorization.
      bins = [0, 167, 1000]
      labels = ['Normal', 'High']
      df['CAT_Insulin'] = pd.cut(df['Insulin'], bins=bins, labels=labels, right=False)

      # Let's create bins for our BMI categorization.
      bins = [0, 18.6, 25.0, 30.0, 100]
      labels = ['Underweight', 'Normal', 'Overweight', 'Obese']
      df['CAT_BMI'] = pd.cut(df['BMI'], bins=bins, labels=labels, right=False)
      

      cat_cols = ['CAT_Pregnancies', 'CAT_Glucose', 'CAT_BloodPressure', 'CAT_Insulin', 'CAT_BMI']
      num_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    
      # One-Hot Encoder
      # download the file before loading it with joblib
      one_hot_encoder_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/models/diabetes_onehot_encoder.joblib')
      onehot_encoder = joblib.load(one_hot_encoder_file)
      
      
      # Transform the categorical data using the loaded encoder
      encoded_data = onehot_encoder.transform(df[cat_cols])
      
      # Convert the encoded data to a DataFrame with the full set of column names
      encoded_df = pd.DataFrame(encoded_data, columns=onehot_encoder.get_feature_names_out(cat_cols))
      
      # Drop the original categorical columns from X1
      X_encoded = df.drop(columns=cat_cols)
      
      # Combine the numerical data with the encoded categorical data
      X_encoded = pd.concat([X_encoded, encoded_df], axis=1)
  
      
  
      # Get scaler file
      scaler_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/models/diabetes_minmax_scaler.pkl')
      scaler = joblib.load(scaler_file)
      X_encoded[num_cols] = scaler.transform(X_encoded[num_cols])
      
      # Predicting Case with imported model
      model_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/models/diabetes_rf_model.joblib')
      rf_model = joblib.load(model_file)
      predicted = rf_model.predict_proba(X_encoded)
  
      no = f'{predicted[0][0] * 100:.2f}%'
      yes = f'{predicted[0][1] * 100:.2f}%'
      
      if np.argmax(predicted) == 0:
          st.subheader('Not Diabetic')
          st.write(f'Patient has a {no} chance of NOT being Diabetic')
      else:
          st.subheader('Diabetic')
          st.write(f'Patient has a {yes} chance of being Diabetic')
      
      results = pd.DataFrame([[no, yes]], columns=['Not Diabetic', 'Diabetic'])
      st.write(results)
      

if __name__ == "__main__":
    diabetes_predictor()
