import streamlit as st
from lbw import lbw_predictor
from ptd import ptd_predictor
from diabetes import diabetes_predictor




st.markdown("""
    <style>
    .centered-title {
            display: flex; justify-content: center; align-items: center; text-align: center; margin: 0; font-size: 3em; font-weight: bold;
            }
    /* Responsive design for smaller screens */
    @media (max-width: 600px) {.centered-title {font-size: 2.0em;}}
    </style>

    <div class="centered-title">MARTERNAL HEALTHCARE</div>
""", unsafe_allow_html=True)


condition = st.selectbox(
    "",
    ["Select Health Condition", "Preterm Delivery", "Low Birth Weight", "Diabetes"]
)
    

if condition == "Preterm Delivery":
    ptd_predictor()
elif condition == "Low Birth Weight":
    lbw_predictor()
elif condition == "Diabetes":
    diabetes_predictor()
