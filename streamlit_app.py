import streamlit as st
import pandas as pd
import numpy as np


st.title('Low Birth Weight Predictor')

col1, col2 = st.columns(2)
with col1:
  age = st.number_input('Age')
with col2:
  levelofeducation = st.selectbox('Level of education', ['Secondary', 'Illiterate', 'Tertiary', 'Basic'])

col1, col2 = st.columns(2)
with col1:
  occupation = st.selectbox('Occupation', ['Self employed', 'Unemployed', 'Civil Servant', 'Other'])
with col2:
  occupation = st.selectbox('Occupation', ['B Pos', 'O Pos', 'O Neg', 'A Pos', 'A Neg', 'AB Pos', 'B Neg', 'AB Neg'])
