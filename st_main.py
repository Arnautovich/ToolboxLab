import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.image('./images/dist_img.png', use_column_width=True)


    st.page_link("pages/st_Distillation.py", label="Binary distillation")
    #center page link
    st.markdown("<h1 style='text-align: center;'>Distillation</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Binary distillation</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>This app calculates the number of distillation states needed for a binary distillation column.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>The McCabe-Thiele diagram is used to determine the number of distillation states needed for a binary distillation column.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>The inputs are the following:</p>", unsafe_allow_html=True)
    #link to the Distillation.py file
    st.markdown("<p style='text-align: center;'>F: Feed flow rate</p>", unsafe_allow_html=True)

    

