import streamlit as st
import Toolbox.LLE as tl 

st.header("Liquid-Liquid Extraction")

st.write("Are you considering cross-flow or counter-flow ?")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    <div style='text-align: right;'>
        Cross-flow
    </div>
    """,
    unsafe_allow_html=True
)

with col2:
    tog = st.toggle("Counter-flow")