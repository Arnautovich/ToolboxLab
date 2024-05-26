import streamlit as st
import Toolbox.LLE as tl 

st.header("Liquid-Liquid Extraction")

st.write("Are you considering cross-flow or counter-flow ?")
col1, col2 = st.columns(2)

with col1:
    st.markdown(
    """
    <div style='text-align: right;'>
        Counter-flow
    </div>
    """,
    unsafe_allow_html=True)
    R = st.number_input("Select R:", 0.0, value=100.0, help="The raffinate flow rate")
    E = st.number_input("Select E:", 0.0, value=100.0, help="The extracted solvant flow rate")
    kD = st.number_input("Select kD:", 0.0000001, value=1.6, help="The relative volatility of the light component with respect to the heavy one")

with col2:
    tog = st.toggle("Cross-flow")
    x0 = st.slider("Select x0:", 0.00, 1.00, 0.02,step=10**(-2), help="The feed composition")
    xN = st.slider("Select xN:", 0.00, x0, 0.002, step=10**(-3), help="The output raffinate composition")
    yN1 = st.slider("Select yN_1:", 0.0, 1.0, 0.0, help="The input solvant composition")

if tog == False:
    fig, stages = tl.lle(R=R, E=E, x0=x0, xN=xN, yN_1=yN1, kD=kD)
else:
    fig, stages = tl.LLE_cross_flow(R=R, E=E, x0=x0, xN=xN, y_in=yN1, kD=kD)

st.write(f"The values selected are: R = {R}, E = {E}, x0 = {x0}, xN = {xN}, yN_1 = {yN1} and kD = {kD}")
st.subheader(f"The number of stages necessary are {stages}")
fig

# mettre unité dans help
# Précision pour kD -> plage de données pour kD ? 