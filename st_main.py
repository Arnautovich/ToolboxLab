import streamlit as st

st.write("test test")

col1, col2 = st.columns(2)

with col1:
    st.image('./images/dist_img.png', use_column_width=True)

    st.page_link("pages/st_Distillation.py", label="Binary distillation")

