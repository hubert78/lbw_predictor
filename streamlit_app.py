import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib
from sklearn.svm import SVC


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
st.title('Low Birth Weight Predictor')

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
    ptd37weeks = st.selectbox('37 weeks pregnant', yes_no_option, index=yes_no_option.index('No'))
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
        retro, bloodgroup, gestational_age, ptd37weeks, sbp, dbp, antpartumhemorrhage, eclampsia, severe_eclampsia, babysex,  
    ]
    
    col_names = [
        'MATERNALAGE', 'LEVELOFEDUCATION', 'OCCUPATION', 'GRAVIDITY', 'PARITY','NO.ANTENALVISITS', 'HB_Delivery', 
        'HEPATITISBSTATUS', 'SYPHILLISSTATUS', 'RETROSTATUS', 'BLOODGROUP', 'GESTATIONALAGE', 'PTDlt37WEEKS', 
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
    categorical_columns = [
        'CAT_MATERNALAGE', 'LEVELOFEDUCATION', 'OCCUPATION', 'CAT_GRAVIDITY', 'CAT_PARITY',
        'HEPATITISBSTATUS', 'SYPHILLISSTATUS', 'RETROSTATUS', 'BLOODGROUP', 'PTDlt37WEEKS', 
        'AntepartumHemorrhage', 'ECLAMPSIA', 'SEVEREPREECLAMPSIA', 'BABYSEX'
    ]
    
    
    numerical_columns = ['MATERNALAGE', 'GRAVIDITY', 'PARITY', 'NO.ANTENALVISITS', 'HB_Delivery', 'GESTATIONALAGE', 
                   'SBPBEFOREDELIVERY', 'DBPBEFOREDELIVERY']
    
    # One-Hot Encoder
    onehot_encoder = joblib.load('https://github.com/hubert78/lbw_predictor/raw/master/onehot_encoder.joblib')

    st.write(onehot_encoder)
    expected_features = onehot_encoder.get_feature_names_out()
    st.write(expected_features)
    # Ensure the DataFrame has all the necessary columns
    missing_columns = [col for col in categorical_columns if col not in df.columns]
    if missing_columns:
        st.warning(f"The following columns are missing from the DataFrame: {missing_columns}")
    
    
    encoded_data = onehot_encoder.transform(df[categorical_columns])
    # Convert the encoded data to a DataFrame with proper column names
    encoded_df = pd.DataFrame(encoded_data, columns=onehot_encoder.get_feature_names_out(categorical_columns))
    # Drop the original categorical columns from X
    X_encoded = df.drop(columns=categorical_columns)
    # Combine the numerical data with the encoded categorical data
    X_encoded = pd.concat([X_encoded, encoded_df], axis=1)
    
    
    
    scaler = joblib.load('https://github.com/hubert78/lbw_predictor/raw/master/minmax_scaler.pkl')
    X_encoded[numerical_columns] = scaler.transform(df[numerical_columns])
    
    # Predicting Case with imported model
    loaded_svm_model = joblib.load('https://github.com/hubert78/lbw_predictor/raw/master/LBW-svm-model.joblib')
    predicted = loaded_svm_model.predict([X_encoded.iloc[0]])
    
    if predicted == 0:
        st.success('Patient had little chance of delivering a low birth weight baby')
    else:
        st.warning('Patient has a high chance of delivering a low birth weight baby')
    
    
    
