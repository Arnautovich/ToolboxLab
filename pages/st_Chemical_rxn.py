import streamlit as st
from chemical_rxn import equation

reac = st.text_input("Please enter your reaction as follow [list of reactants] -> [list of products] : ", 
                     help="If your text doesn't work try different names for your compounds")