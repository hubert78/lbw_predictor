import streamlit as st
import pandas as pd
import numpy as np


st.title('Low Birth Weight Predictor')

levelofeducation_options = ['Basic', 'Illiterate', 'Secondary', 'Tertiary']
occupation_options = ['Civil Servant', 'Self employed', 'Unemployed', 'Other']
bloodgroup = ['A Neg', 'A Pos', 'AB Neg', 'AB Pos', 'B Neg', 'B Pos', 'O Neg', 'O Pos']
serology_test = ['Non Reactive', 'Reactive']


st.write('Patient socio-demographic details')
col1, col2 = st.columns(2)
with col1:
  maternal_age = st.number_input('Maternal age', min_value=10, max_value=50, value=26)
with col2:
  levelofeducation = st.selectbox('Level of education', levelofeducation_options, index=levelofeducation_options.index('Illiterate'))

col1, col2 = st.columns(2)
with col1:
  occupation = st.selectbox('Occupation', occupation_options, index=occupation_options.index('Self employed'))



st.write('Pregnancy history')
col1, col2 = st.columns(2)
with col1:
  occupation = st.number_input('Gravidity', min_value=1, max_value=10, value=1)
with col2:
  occupation = st.number_input('Parity', min_value=0, max_value=10, value=0  )

col1, col2 = st.columns(2)
with col1:
  antenatal_visits = st.number_input('Number of antenatal visits', min_value=0, max_value=20, value=7)
with col2:
  gestational_age = st.number_input('Gestational age', min_value=20, max_value=43, value=38)


st.write('Laboratory results')
col1, col2 = st.columns(2)
with col1:
  bloodgroup = st.selectbox('Blood Type', bloodgroup, index=bloodgroup.index('O Pos'))
with col2:
  hepatitis = st.selectbox('Hepatitis B Status', serology_test, index=serology_test.index('Non Reactive'))
  
col1, col2 = st.columns(2)
with col1:
  retro = st.selectbox('Retro (HIV) Status', serology_test, index=serology_test.index('Non Reactive'))
with col2:
  syphillis = st.selectbox('Syphillis Status', serology_test, index=serology_test.index('Non Reactive'))
