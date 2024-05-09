import streamlit as st
from pathlib import Path

#path image for mac and windows
path = Path(__file__).parent
path = str(path) + '/images/dist_img.png'




col1, col2 = st.columns(2)

app_path = 'http://localhost:8501'
page_file_path = 'pages/st_Distillation.py'
page1 = page_file_path.split('/')[1][0:-3]  # get "page1"


with col1:
    st.image(path, use_column_width=True)


    st.markdown(f'''<h3 style='text-align: center;'><a href="{app_path}/{page1}" target="_self">Distillation</a></h3>''',
    unsafe_allow_html=True
)
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
    st.markdown("<p style='text-align: center;'>This app calculates the number of distillation states needed for a binary distillation column.</p>", unsafe_allow_html=True)
    


    

