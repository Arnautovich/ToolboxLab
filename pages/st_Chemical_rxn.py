import streamlit as st
from chemical_rxn import equation

reac = st.text_input("Please enter your reaction as follow [list of reactants] -> [list of products] : ", 
                     help="If your text doesn't work try different names for your compounds")

rxn = equation(reac)

st.image(rxn.draw_reaction())

tog1 = st.toggle("View products properties", help="")
if tog1:
    st.dataframe(rxn.get_reaction_properties())

# description du tableau + input par default dans box + modifier text input
