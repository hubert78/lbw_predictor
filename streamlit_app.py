import streamlit as st
from lbw import lbw_predictor
from ptd import ptd_predictor




st.title('MARTERNAL HEALTHCARE')

col1, col2 = st.columns(2)

with col1:
    condition = st.radio("Select Health Condition", ["Preterm Delivery"])
    
with col2:
    condition = st.radio("", ["Low Birth Weight"])
    

if condition == "Preterm Delivery":
    ptd_predictor()
elif condition == "Low Birth Weight":
    lbw_predictor()
