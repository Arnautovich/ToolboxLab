import streamlit as st
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp

st.header("Converte molecule name to SMILES")

name = st.text_input("The name of your molecule:")
el = tc.elements(name)

smile = el.smile
prop = el.properties
