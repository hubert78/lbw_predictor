import streamlit as st
import pandas as pd
import numpy as np


# Function to categorize some numeric columns 
def categorize_column(df, column_name, bins):
    num_of_categories = len(bins) - 1
    labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(num_of_categories)]
    
    if column_name in df.columns:
        df['CAT_' + column_name] = pd.cut(df[column_name], bins=bins, labels=labels, right=False)
    else:
        print("Column '%s' does not exist in the DataFrame." % column_name)
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
    dbp = st.selectbox('Severe Eclampsia', yes_no_option, index=yes_no_option.index('No'))

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

if st.button('Check prediction'):
    data_list = [[
        maternal_age, levelofeducation, occupation, gravidity, parity, antenatal_visits, gestational_age,
        ptd37weeks, antpartumhemorrhage, sbp, dbp, babysex, bloodgroup, hb, retro, syphillis, hepatitis
    ]]
    
    col_names = [
        'MATERNALAGE', 'LEVELOFEDUCATION', 'OCCUPATION', 'GRAVIDITY', 'PARITY', 'NO.ANTENALVISITS', 'GESTATIONALAGE',
        'PTDlt37WEEKS', 'AntepartumHemorrhage', 'SBPBEFOREDELIVERY', 'DBPBEFOREDELIVERY', 'BABYSEX', 
        'BLOODGROUP', 'HB_Delivery' 'RETROSTATUS', 'SYPHILLISSTATUS', 'HEPATITISBSTATUS'
    ]
    
    df = pd.DataFrame(data_list, columns=col_names)
    st.write(df)
    st.write(data_list)

