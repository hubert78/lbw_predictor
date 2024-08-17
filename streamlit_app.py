import streamlit as st
import pandas as pd
import numpy as np


st.title('Low Birth Weight Predictor')

1col1, 1col2 = st.columns(2)
with 1col1:
  age = st.number_input('Age')
with 1col2:
  levelofeducation = st.selectbox('Level of education', ['Secondary', 'Illiterate', 'Tertiary', 'Basic'])

2col1, 2col2 = st.columns(2)
with 2col1:
  occupation = st.selectbox('Occupation', ['Self employed', 'Unemployed', 'Civil Servant', 'Other'])
with 2col2:
  occupation = st.selectbox('Occupation', ['B Pos', 'O Pos', 'O Neg', 'A Pos', 'A Neg', 'AB Pos', 'B Neg', 'AB Neg'])
