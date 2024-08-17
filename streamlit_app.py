import streamlit as st
import pandas as pd
import numpy as np


st.title('Low Birth Weight Predictor')

levelofeducation_options = ['Basic', 'Illiterate', 'Secondary', 'Tertiary']
occupation_options = ['Civil Servant', 'Self employed', 'Unemployed', 'Other']
bloodgroup = ['A Neg', 'A Pos', 'AB Neg', 'AB Pos', 'B Neg', 'B Pos', 'O Neg', 'O Pos']


col1, col2 = st.columns(2)
with col1:
  age = st.number_input('Age')
with col2:
  levelofeducation = st.selectbox('Level of education', levelofeducation_options, index=levelofeducation_options.index('Basic'))

col1, col2 = st.columns(2)
with col1:
  occupation = st.selectbox('Occupation', occupation_options, index=occupation_options.index('Civil Servant'))
with col2:
  bloodgroup = st.selectbox('Blood Type', bloodgroup, index=bloodgroup.index('O Pos'))

col1, col2 = st.columns(2)
with col1:
  occupation = st.number_input('Gravidity')
with col2:
  occupation = st.number_input('Parity')

col1, col2 = st.columns(2)
with col1:
  occupation = st.number_input('Number of antenatal visits', min_value=0, max_value=30, value=10)
with col2:
  occupation = st.number_input('Gestational age', min_value=20, max_value=43, value=37)




