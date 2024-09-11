import streamlit as st
from lbw import lbw_predictor
from ptd import ptd_predictor
from diabetes import diabetes_predictor




st.title('MARTERNAL HEALTHCARE')

condition = st.selectbox(
    "",
    ["Select Health Condition", "Preterm Delivery", "Low Birth Weight", "Diabetes"]
)
    

if condition == "Preterm Delivery":
    ptd_predictor()
elif condition == "Low Birth Weight":
    lbw_predictor()
else:
    diabetes_predictor()
