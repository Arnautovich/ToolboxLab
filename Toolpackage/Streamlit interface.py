import streamlit as st
from function import funct 

st.write("hello **world** !")

"visualisation : normal, **gras**, __gras__, _italique_, *italique*, $LaTeX$, :smile:, "

st.line_chart([1,2,8,6])

temp = st.slider('choose your temperature : ')
pression = st.slider('choose your pressure : ')



st.write(f"The pressure of rotavap is {temp*pression/2} with temp = {temp} and pressure = {pression}")

st.write("the result of the function is ",funct(2,3)) 
