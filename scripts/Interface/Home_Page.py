import streamlit as st
from pathlib import Path

#path image for mac and windows
path = Path(__file__).parent
path_img1 = str(path) + '/images/dist_img.png'
path_img2 = str(path) + '/images/chem_img.png'
path_img3 = str(path) + '/images/PH_img.png'

col1, col2 = st.columns(2)

app_path = 'http://localhost:8501'
page_file_path1 = 'pages/Distillation.py'
page_file_path2 = 'pages/Chemical_Reaction.py'
page_file_path3 = 'pages/pH_Calculator.py'
page_file_path4 = 'pages/Liquid-Liquid_Extraction.py'
page_file_path5 = 'pages/Boiling_Point_at_new_Pressure.py'

page1 = page_file_path1.split('/')[1][0:-3]  # get "page1"
page2 = page_file_path2.split('/')[1][0:-3]  # get "page2"
page3 = page_file_path3.split('/')[1][0:-3]
page4 = page_file_path4.split('/')[1][0:-3]
page5 = page_file_path5.split('/')[1][0:-3]

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
        ''', unsafe_allow_html=True
    )
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
    st.markdown("description", unsafe_allow_html=True)

    st.image(path_img3, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page3}" target="_self">Boiling Point at new Pressure</a></h3>''',
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
    st.markdown("description", unsafe_allow_html=True)
    

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
        ''', unsafe_allow_html=True
    )

    #Stoitometry of chemical reaction and properties of the reactants
    st.markdown("<p style='text-align: center;'>This app calculates the stoichiometry of a chemical reaction and the properties of the reactants/products.</p>", unsafe_allow_html=True)
    
    st.image(path_img1, use_column_width=True)

    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page4}" target="_self">Liquid-Liquid Extraction</a></h3>''',
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
        ''', unsafe_allow_html=True
    )
    st.markdown("description", unsafe_allow_html=True)

