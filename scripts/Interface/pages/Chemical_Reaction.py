import streamlit as st
from Toolbox.chemical_rxn import equation

st.header("Chemical Reaction")

reac = st.text_input('''Please enter your reaction as follow:  
                     reactant1 + reactant2 + ... -> product1 + product2 + ...''', 
                     help="If your text doesn't work try different names for your compounds",
                     placeholder="NaOH + HCl -> H2O + NaCl   or   methane + O2 -> water + CO2")

if reac != "":
    rxn = equation(reac)
    st.image(rxn.draw_reaction())

    st.dataframe(rxn.get_reaction_properties())
    
    st.write('''In this data frame:  
             - Stoichiometric coefficients are negative for reactants and positive for products  
             - Molecular weights are indicated in g/mol
             ''')

# description du tableau + input par default dans box + modifier text input     