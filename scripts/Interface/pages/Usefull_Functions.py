import streamlit as st
import pandas as pd
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp
import Toolbox.MSDS as msds

st.header("Converte molecule name to SMILES")

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

