import streamlit as st
from lbw import lbw_predictor
from ptd import ptd_predictor




st.title('MARTERNAL HEALTHCARE')

condition = st.radio(
    "Select Health Condition",
    ["Preterm Delivery", "Low Birth Weight"],
    horizontal=st.session_state.horizontal,
)

if condition == "Preterm Delivery":
    ptd_predictor()
elif condition == "Low Birth Weight":
    lbw_predictor()
