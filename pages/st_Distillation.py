import streamlit as st
from Distillation import distillation 

col1, col2 = st.columns(2)

with col1:
    F = st.number_input("Select F :", min_value=0.0, max_value=200.0, value=100.0, step=1.0, help="Feed")
    D = st.number_input("Select D :", min_value=0.0, max_value=100.0, value=50.0, step=1.0, help="Distillate flow rate")
    st.toggle("Take xB in account instead of D", help="If enable : The value of D will be ignore in the calculations")
    q = st.number_input("Select q :", min_value=0.0, max_value=200.0, value=1.0, step=0.1, help="Feed quality")
    alpha = st.number_input("Select alpa :", min_value=0.0, max_value=20.0, value=10.0, step=1.0, help="Relative volatility")

with col2:
    z = st.slider("Select z :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Fraction of product in the feed")
    xD = st.slider("Select xD :", min_value=z+0.05, max_value=1.0, value=0.9, step=0.05, help="Fraction of product in the distillate")
    R = st.slider("Select R :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Reflux ratio [L/D]")
    xB = st.slider("Select xB :", min_value=0.0, max_value=1.0, value=0.5, step=0.1, help="Fraction of product in bottom flow")

number, fig = distillation(F=F, xD=xD, R=R, z=z, q=q, alpha=alpha, xB=xB, D=D)

st.write(f"The number of distillation states needed are {number}")
fig 