import streamlit as st
from Toolbox.Distillation import distillation 

col1, col2 = st.columns(2)

with col1:
    F = st.number_input("Select F :", min_value=0.0, max_value=200.0, value=100.0, step=1.0, help="Feed")
    D = st.number_input("Select D :", min_value=0.0, max_value=100.0, value=50.0, step=1.0, help="Distillate flow rate")
    z = st.slider("Select z :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Fraction of product in the feed")
    xD = st.slider("Select xD :", min_value=z, max_value=1.0, value=0.6, step=0.1, help="Fraction of product in the distillate")
with col2:
    q = st.number_input("Select q :", min_value=0.0, max_value=200.0, value=1.0, step=1.0, help="Feed quality")
    alpha = st.number_input("Select alpa :", min_value=0.0, max_value=20.0, value=10.0, step=1.0, help="Relative volatility")
    R = st.slider("Select R :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Reflux ratio [L/D]")
    xB = st.slider("Select xB :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Fraction of product in bottom flow")
number, fig = distillation(F, D, xD, R, z, q, alpha)

st.write(f"The number of distillation states needed are {number}")
fig 