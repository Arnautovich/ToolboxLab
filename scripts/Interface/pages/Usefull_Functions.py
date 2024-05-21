import streamlit as st
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp

st.header("Usefull Functions")

st.subheader("Converte molecule name to SMILES")

name = st.text_input("The name of your molecule:", value="Water", help="If the name used does not work, try different names for your compound")
el = tc.elements(name)

smile = el.smile
prop = el.properties
nbre = el.atoms_nb

st.write(f'''The smile of {name} is: {smile}  
The atom list is : {nbre}  
usefull properties are :''')
st.dataframe(prop, width=700)
