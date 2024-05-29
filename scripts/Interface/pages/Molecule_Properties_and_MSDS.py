import streamlit as st
import pandas as pd
import requests
import Toolbox.chemical_rxn as tc
import Toolbox.Pressure_TB as tp
import Toolbox.MSDS as ms2
import rdkit

st.header("Molecule Properties and MSDS")

name = st.text_input("The name of your molecule:", value=None, help="If the name used does not work, try different names for your compound")
if name != None:
    el = tc.elements(name)

    smile = el.smile
    prop = el.properties
    nbre = el.atoms_nb
    cas = tp.resolve_name_to_cas(molecule_name=name)

    if "[" in smile:
        smile = smile.replace("[", "\[")

    st.write(f'''The **SMILE** of {name} is: {smile}  
    The **CAS** number is: {cas}  
    The atom list is: {nbre}  
    Usefull properties are:''')
    st.dataframe(prop, width=700)

    st.write('''In this data frame:  
             - CID is the PubChem Compound Identifier  
             - Molecular weight is indicated in g/mol  
             - Canonical SMILES is the unique SMILES representation of the molecule  
             - IUPAC name is the name of the molecule according to the International Union of Pure and Applied Chemistry  
             - XlogP is the partition coefficient of the molecule between n-octanol and water  
             - Monoisotopic mass is the sum of the atomic masses of the most common isotope of each element in the molecule, indicated in g/mol  
             - H bond donor / acceptor count is the number of hydrogen bonds that can be donated or accepted by the molecule  
             ''')

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
