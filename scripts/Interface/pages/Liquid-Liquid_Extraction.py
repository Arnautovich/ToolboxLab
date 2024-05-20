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
    R = st.number_input("The raffinate flow rate R:", 0.0, value=100.0)
    E = st.number_input("The extracted solvant flow rate E:", 0.0, value=100.0)
    kD = st.number_input("The relative volatility of the light component with respect to the heavy one kD:", 0.0, value=1.6)

with col2:
    tog = st.toggle("Cross-flow")
    x0 = st.slider("The feed composition x0:", 0.00, 1.00, 0.018)
    xN = st.slider("The output raffinate composition xN:", 0.00, x0, 0.002, step=10**(-4))
    yN1 = st.slider("The input solvant composition yN_1:", 0.0, 1.0, 0.0)

if tog == False:
    fig, stages = tl.lle(R=R, E=E, x0=x0, xN=xN, yN_1=yN1, kD=kD)
else:
    fig, stages = tl.LLE_cross_flow(R=R, E=E, x0=x0, xN=xN, y_in=yN1, kD=kD)

st.write(f"The number of stages necessary are {stages}")
fig

# rajouter help
# 