import streamlit as st
from Toolbox.chemical_rxn import equation

col1, col2 = st.columns(2)

with col1:
    tog1 = st.toggle("View image of reaction", value=True)

with col2:
    tog2 = st.toggle("View products properties", value=True)

reac = st.text_input('''Please enter your reaction as follow:  
                     reactant1 + reactant2 + ... -> product1 + product2 + ...''', 
                     help="If your text doesn't work try different names for your compounds",
                     placeholder="NaOH + HCl -> H2O + NaCl   or   methane + O2 -> water + CO2")

if reac != "":
    rxn = equation(reac)
    if tog1:
        st.image(rxn.draw_reaction())

    st.write('''In this data frame:  
             Stoichiometric coefficients are negative for reactants and positive for products''')
    if tog2:
        st.dataframe(rxn.get_reaction_properties())

# description du tableau + input par default dans box + modifier text input 