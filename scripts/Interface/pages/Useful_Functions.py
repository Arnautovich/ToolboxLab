import streamlit as st
import pandas as pd
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp
import Toolbox.MSDS as msds

st.header("Usefull Functions")


# ce que j'ai écrit avant de pull mdrrr :

st.subheader("Molecule Description")

name = st.text_input("The name of your molecule:", value="methane", help="If the name used does not work, try different names for your compound")
el = tc.elements(name)

smile = el.smile
prop = el.properties
nbre = el.atoms_nb
cas = tp.resolve_name_to_cas(name)

st.write(f'''The **SMILE** of {name} is: {smile}  
The **CAS** number is: {cas}  
The atom list is: {nbre}  
Usefull properties are:''')
st.dataframe(prop, width=700)

list_comp = ["Sigma-Aldrich", ""]

company = st.selectbox("From which company do you want your MSDS sheet ?", list_comp)

st.write(f"The **MSDS sheet** of {name} from {company} is:")
sec = msds.display_pdf_images(name)
sec

name = st.text_input("The name of your molecule:")

if name != "":
    el = tc.elements(name)

    smile = el.smile
    prop = el.properties

    columns = ['MolecularWeight','IUPACName','CanonicalSMILES', 'MonoisotopicMass', 'HBondDonorCount', 'HBondAcceptorCount','XLogP']

    prop = pd.DataFrame([prop], columns=columns)

    cas = tp.resolve_name_to_cas(name)

    security = msds.display_pdf_images(name)

    if "html" in cas:
        st.write("The CAS number was not found")
        st.write("Please input the CAS number manually")
        cas = st.text_input("CAS number:")
    

    st.write(f"SMILES: {smile}")
    st.write(f"CAS: {cas}")
    st.dataframe(prop)
    st.image(security)
