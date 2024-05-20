import streamlit as st
import Toolbox.pH as tp

st.header("What do you want to calculate :")

col1, col2 = st.columns(2)

with col1:

    comp = st.radio("Which compound do you need ?", ["Strong acid", "Strong base", "Weak acid", "Weak base", "Buffer solution"], index=None)

with col2:

    val = st.radio("Which value do you need ?", ["pH", "Concentration"], index=None)

if comp == "Strong acid" and val == "pH":
    ca = st.number_input("The concentration of your acid (mol/L):", 0.0, step= 10**(-5))
    pH = tp.strongacidpH(ca)
    st.write(f"The pH calculated is {pH}")

elif comp == "Strong acid" and val == "Concentration":
    ca = 

if __name__ == "__main__":
    st.write(comp)
    st.write(val)
