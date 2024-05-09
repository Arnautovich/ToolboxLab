import streamlit as st
from chemical_rxn import equation

col1, col2 = st.columns(2)

with col1:
    tog1 = st.toggle("View image of reaction")

with col2:
    tog2 = st.toggle("View products properties", help="")

reac = st.text_input("Please enter your reaction as follow [list of reactants] -> [list of products] : ", 
                     help="If your text doesn't work try different names for your compounds",
                     placeholder="NaOH + HCl -> H2O + NaCl")

if reac != "":
    rxn = equation(reac)
    if tog1:
        st.image(rxn.draw_reaction())

    if tog2:
        st.dataframe(rxn.get_reaction_properties())

# description du tableau + input par default dans box + modifier text input
