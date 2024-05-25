import streamlit as st
import pandas as pd
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp
import Toolbox.MSDS3 as ms3

st.header("Molecule Properties and MSDS")

st.subheader("Molecule Description")

name = st.text_input("The name of your molecule:", value="methane", help="If the name used does not work, try different names for your compound")
el = tc.elements(name)

smile = el.smile
prop = el.properties
nbre = el.atoms_nb
cas = tp.resolve_name_to_cas(molecule_name=name)

st.write(f'''The **SMILE** of {name} is: {smile}  
The **CAS** number is: {cas}  
The atom list is: {nbre}  
Usefull properties are:''')
st.dataframe(prop, width=700)

list_comp = ms3.list_of_succesful_companies(name)

company = st.selectbox("From which company do you want your **MSDS sheet** ?", list_comp)

st.write(f"The **MSDS sheet** of {name} from {company} is:")
sec = ms3.display_pdf_images(molecule_name=name, company=company)
if sec is not None:
    st.image(sec)
