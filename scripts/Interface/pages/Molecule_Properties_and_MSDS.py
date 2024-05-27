import streamlit as st
import pandas as pd
import requests
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp
import Toolbox.MSDS as ms2
import rdkit

st.header("Molecule Properties and MSDS")

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

list_comp = ms2.new_list_companies(name)

st.image(rdkit.Chem.Draw.MolToImage(rdkit.Chem.MolFromSmiles(smile)))

st.write("From which company do you want your **MSDS sheet** ?")



company = st.selectbox(".", list_comp, label_visibility="collapsed")

pdf_url = f"https://www.chemblink.com/MSDS/MSDSFiles/{cas}{company}.pdf"
response = requests.get(pdf_url)
pdf_bytes = response.content
st.download_button(
    label="Download PDF",
    data=pdf_bytes,
    file_name=f"MSDS-{name}-{company}.pdf",
    mime="application/pdf"
)

st.write(f"The **MSDS sheet** of {name} from {company} is:")
sec = ms2.display_pdf_images(molecule_name=name, company=company)
if sec is not None:
    st.image(sec)

