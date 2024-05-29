import streamlit as st
from pathlib import Path

#path image for mac and windows
path = Path(__file__).parent
path_img1 = str(path) + '/images/dist_img.png'
path_img2 = str(path) + '/images/chem_img.png'
path_img3 = str(path) + '/images/PH_img.png'
path_img4 = str(path) + '/images/lle_img.png'
path_img5 = str(path) + '/images/pressure.png'
path_img6 = str(path) + '/images/msds.png'
path_img7 = str(path) + '/images/solvent.png'

col1, col2 = st.columns(2)

app_path = 'http://localhost:8501'
page_file_path1 = 'pages/Distillation.py'
page_file_path2 = 'pages/Chemical_Reaction.py'
page_file_path3 = 'pages/pH_Calculator.py'
page_file_path4 = 'pages/Liquid-Liquid_Extraction.py'
page_file_path5 = 'pages/Boiling_Point_at_new_Pressure.py'
page_file_path6 = 'pages/Molecule_Properties_and_MSDS.py'
page_file_path7 = 'pages/Solvent_Determination.py'

page1 = page_file_path1.split('/')[1][0:-3]  # get "page1"
page2 = page_file_path2.split('/')[1][0:-3]  # get "page2"
page3 = page_file_path3.split('/')[1][0:-3]
page4 = page_file_path4.split('/')[1][0:-3]
page5 = page_file_path5.split('/')[1][0:-3]
page6 = page_file_path6.split('/')[1][0:-3]
page7 = page_file_path7.split('/')[1][0:-3]


with col1:
    st.image(path_img1, use_column_width=True)


    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page1}" target="_self">Distillation</a></h3>''',
    unsafe_allow_html=True)
    #remove the blue color and underline of the link
    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This app calculates the number of distillation states needed for a binary distillation column.<br />&nbsp;</p>", unsafe_allow_html=True) # <br />&nbsp;
    

    st.image(path_img3, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page3}" target="_self">pH Calculator</a></h3>''',
    unsafe_allow_html=True)
    
    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True
    )
    st.markdown("<p style='text-align: center;'> This app calculates the pH of a solution given some information about the solution.<br />&nbsp;</p>", unsafe_allow_html=True)

    st.image(path_img5, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page5}" target="_self">Boiling Point at new Pressure</a></h3>''',
    unsafe_allow_html=True)
    
    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True
    )
    st.markdown("<p style='text-align: center;'> This app calculates the boiling point of a liquid at a new pressure.<br />&nbsp;</p>", unsafe_allow_html=True)
    
    st.image(path_img7, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page7}" target="_self">Solvent Determination</a></h3>''',
    unsafe_allow_html=True)
    
    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True
    )
    st.markdown("<p style='text-align: center;'> This app rank solvent depending on their application to suit the desired properties the best.<br />&nbsp;</p>", unsafe_allow_html=True)
    

with col2:
    st.image(path_img2, use_column_width=True)


    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page2}" target="_self">Chemical reaction</a></h3>''',
    unsafe_allow_html=True)
    
    #remove the blue color and underline of the link
    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True)

    #Stoichiometry of chemical reaction and properties of the reactants
    st.markdown("<p style='text-align: center;'>This app calculates the stoichiometry of a chemical reaction and the properties of the reactants/products.</p>", unsafe_allow_html=True)
    
    st.image(path_img4, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page4}" target="_self">Liquid-Liquid Extraction</a></h3>''',
    unsafe_allow_html=True)

    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center;'>This app calculates the number of stages needed for a liquid-liquid extraction process.<br />&nbsp;</p>", unsafe_allow_html=True)

    st.image(path_img6, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page6}" target="_self">Molecule Properties and MSDS</a></h3>''',
    unsafe_allow_html=True)

    st.markdown(
        '''
        <style>
        a {
            text-decoration: none;
            color: red;
        }
        </style>
        ''', unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center;'>This app display some properties and the safety data-sheet for a molectule.<br />&nbsp;</p>", unsafe_allow_html=True)
    