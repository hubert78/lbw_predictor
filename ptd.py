import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from io import BytesIO



# Function to download the file from a URL
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return BytesIO(response.content)


# Function to categorize some numeric columns 
def categorize_column(df, col_dict):
    for col in col_dict:
        bins = col_dict[col]
        num_of_categories = len(bins) - 1
        labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(num_of_categories)]
        
        if col in df.columns:
            df['CAT_' + col] = pd.cut(df[col], bins=bins, labels=labels, right=False)

    return df
    


# ---------------- WEB APP STARTS HERE ---------------------------------------
def ptd_predictor():
  st.subheader('Preterm Delivery Prediction')
  
  levelofeducation_options = ['Basic', 'Illiterate', 'Secondary', 'Tertiary']
  occupation_options = ['Civil Servant', 'Self employed', 'Unemployed', 'Other']
  bloodgroup = ['A Neg', 'A Pos', 'AB Neg', 'AB Pos', 'B Neg', 'B Pos', 'O Neg', 'O Pos']
  serology_test = ['Non Reactive', 'Reactive']
  yes_no_option = ['No', 'Yes']
  sex = ['Female', 'Male']
  
  
  
  with st.expander('Patient socio-demographic details'):
    col1, col2 = st.columns(2)
    with col1:
      maternal_age = st.number_input('Maternal age', min_value=10, max_value=50, value=26)
    with col2:
      levelofeducation = st.selectbox('Level of education', levelofeducation_options, index=levelofeducation_options.index('Illiterate'))
    
    col1, col2 = st.columns(2)
    with col1:
      occupation = st.selectbox('Occupation', occupation_options, index=occupation_options.index('Self employed'))
  
  
  
  with st.expander('Clinlical history'):
    col1, col2 = st.columns(2)
    with col1:
      gravidity = st.number_input('Gravidity', min_value=1, max_value=10, value=1)
    with col2:
      parity = st.number_input('Parity', min_value=0, max_value=10, value=0  )
    
    col1, col2 = st.columns(2)
    with col1:
      antenatal_visits = st.number_input('Number of antenatal visits', min_value=0, max_value=20, value=7)
    with col2:
      gestational_age = st.number_input('Gestational age', min_value=20, max_value=43, value=38)
  
    col1, col2 = st.columns(2)
    with col1:
      lbw = st.selectbox('Low Birth Weight', yes_no_option, index=yes_no_option.index('No'))
    with col2:
      antpartumhemorrhage = st.selectbox('Ante-partum Hemorrhage', yes_no_option, index=yes_no_option.index('No'))
  
    col1, col2 = st.columns(2)
    with col1:
      sbp = st.number_input('Systolic blood pressure', min_value=11, max_value=300, value=115)
    with col2:
      dbp = st.number_input('Diastolic blood pressure', min_value=10, max_value=200, value=71)
  
    col1, col2 = st.columns(2)
    with col1:
      eclampsia = st.selectbox('Eclampsia', yes_no_option, index=yes_no_option.index('No'))
    with col2:
      severe_eclampsia = st.selectbox('Severe Eclampsia', yes_no_option, index=yes_no_option.index('No'))
  
    col1, col2 = st.columns(2)
    with col1:
      babysex = st.selectbox('Sex of baby', sex, index=sex.index('Male'))
  
  
  
  with st.expander('Laboratory results'):
    col1, col2 = st.columns(2)
    with col1:
      bloodgroup = st.selectbox('Blood Type', bloodgroup, index=bloodgroup.index('O Pos'))
    with col2:
      hb = st.number_input('Maternal HB', min_value=1.0, max_value=30.0, value=10.6, step=0.1)
      
    col1, col2 = st.columns(2)
    with col1:
      retro = st.selectbox('Retro (HIV) Status', serology_test, index=serology_test.index('Non Reactive'))
    with col2:
      syphillis = st.selectbox('Syphillis Status', serology_test, index=serology_test.index('Non Reactive'))
  
    col1, col2 = st.columns(2)
    with col1:
      hepatitis = st.selectbox('Hepatitis B Status', serology_test, index=serology_test.index('Non Reactive'))
  
  df = pd.DataFrame()
  
  if st.button('Check prediction'):
      data_list = [
          maternal_age, levelofeducation, occupation, gravidity, parity, antenatal_visits, hb, hepatitis, syphillis, 
          retro, bloodgroup, gestational_age, lbw, sbp, dbp, antpartumhemorrhage, eclampsia, severe_eclampsia, babysex,  
      ]
      
      col_names = [
          'MATERNALAGE', 'LEVELOFEDUCATION', 'OCCUPATION', 'GRAVIDITY', 'PARITY','NO.ANTENALVISITS', 'HB_Delivery', 
          'HEPATITISBSTATUS', 'SYPHILLISSTATUS', 'RETROSTATUS', 'BLOODGROUP', 'GESTATIONALAGE', 'LOWBIRTHWEIGHT', 
          'SBPBEFOREDELIVERY', 'DBPBEFOREDELIVERY', 'AntepartumHemorrhage', 'ECLAMPSIA', 'SEVEREPREECLAMPSIA', 'BABYSEX'
      ]
  
      # Wrap data_list in another list to make it a 2D list
      df = pd.DataFrame([data_list], columns=col_names)
  
      # Feature Engineering
      col_dict = {}
      col_dict['MATERNALAGE'] = [0, 21, 36, 100]
      col_dict['GRAVIDITY'] = [1, 2, 3, 10]
      col_dict['PARITY'] = [0, 1, 2, 10]
      
      df = categorize_column(df, col_dict)
      
      
      # Normalization and One-Hot Encoding
      
      # Categorizing the Columns as either a Categorical Column or Numberical Column
      categorical_columns = ['CAT_MATERNALAGE', 'LEVELOFEDUCATION', 'OCCUPATION', 'CAT_GRAVIDITY', 'CAT_PARITY',
          'HEPATITISBSTATUS', 'SYPHILLISSTATUS', 'RETROSTATUS', 'BLOODGROUP', 'LOWBIRTHWEIGHT', 
          'AntepartumHemorrhage', 'ECLAMPSIA', 'SEVEREPREECLAMPSIA', 'BABYSEX']
      
      
      numerical_columns = ['MATERNALAGE', 'GRAVIDITY', 'PARITY', 'NO.ANTENALVISITS', 'HB_Delivery', 'GESTATIONALAGE', 
                     'SBPBEFOREDELIVERY', 'DBPBEFOREDELIVERY']
  
  
      # One-Hot Encoder
      # download the file before loading it with joblib
      one_hot_encoder_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/ptd_onehot_encoder.joblib')
      onehot_encoder = joblib.load(one_hot_encoder_file)
      
      
      # Transform the categorical data using the loaded encoder
      encoded_data = onehot_encoder.transform(df[categorical_columns])
      
      # Convert the encoded data to a DataFrame with the full set of column names
      encoded_df = pd.DataFrame(encoded_data, columns=onehot_encoder.get_feature_names_out(categorical_columns))
      
      # Drop the original categorical columns from X1
      X_encoded = df.drop(columns=categorical_columns)
      
      # Combine the numerical data with the encoded categorical data
      X_encoded = pd.concat([X_encoded, encoded_df], axis=1)
  
      
  
      # Get scaler file
      scaler_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/ptd_minmax_scaler.pkl')
      scaler = joblib.load(scaler_file)
      X_encoded[numerical_columns] = scaler.transform(X_encoded[numerical_columns])
      
      
      # Predicting Case with imported model
      model_file = download_file('https://github.com/hubert78/lbw_predictor/raw/master/ptd-svm-model.joblib')
      loaded_svm_model = joblib.load(model_file)
      predicted = loaded_svm_model.predict_proba(X_encoded)
  
      no = f'{predicted[0][0] * 100:.2f}%'
      yes = f'{predicted[0][1] * 100:.2f}%'
      
      if np.argmax(predicted) == 0:
          st.subheader(f'Patient has a {no} chance of NOT delivering Preterm')
      else:
          st.subheader(f'Patient has a {yes} chance of having a Preterm Delivery')
      
      results = pd.DataFrame([[no, yes]], columns=['No', 'Yes'])
      st.write(results)
      

if __name__ == "__main__":
    ptd_predictor()
