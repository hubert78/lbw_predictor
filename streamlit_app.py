import streamlit as st
import pandas as pd
import numpy as np


st.title('Low Birth Weight Predictor')

options = ['Civil Servant', 'Self employed', 'Unemployed', 'Other']
default_value = 'Self employed'

col1, col2 = st.columns(2)
with col1:
  age = st.number_input('Age')
with col2:
  levelofeducation = st.selectbox('Level of education', index= 'Tertiary', ['Basic', 'Illiterate', 'Secondary', 'Tertiary'])

col1, col2 = st.columns(2)
with col1:
  occupation = st.selectbox('Occupation', ['Civil Servant', 'Self employed', 'Unemployed', 'Other'])
with col2:
  occupation = st.selectbox('Blood Type', ['A Neg', 'A Pos', 'AB Neg', 'AB Pos', 'B Neg', 'B Pos', 'O Neg', 'O Pos'])

col1, col2 = st.columns(2)
with col1:
  occupation = st.number_input('Gravidity')
with col2:
  occupation = st.number_input('Parity')

col1, col2 = st.columns(2)
with col1:
  occupation = st.number_input('Gravidity')
with col2:
  occupation = st.number_input('Parity')




