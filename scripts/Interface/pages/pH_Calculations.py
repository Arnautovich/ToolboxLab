import streamlit as st
import pH_Calculations as pc

st.header("What do you want to calculate :")

col1, col2 = st.columns(2)

with col1:

    comp = st.radio("Which compound do you need ?", ["Strong acid", "Strong base", "Weak acid", "Weak base", "Buffer solution"])

with col2:

    val = st.radio("Which value do you need ?", ["pH", "Concentration"])




st.write(comp)
st.write(val)