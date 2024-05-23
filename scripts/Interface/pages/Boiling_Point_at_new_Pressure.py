import streamlit as st
import Toolbox.Pressure_TB as tp

st.header("Boiling Point at new Pressure")

pres = st.number_input("The pressure of the operation in [bar]:", 0.001, value=1.013, step=0.001)
name = str(st.text_input("The name of the molecule:", value="Water", help="If the molecule doesn't work it is maybe that this molecule is not in the Chemicals package"))

bp = tp.clausius_clapeyron_enthalpy(Pressure=pres, molecule_name=name)
bpatm = tp.clausius_clapeyron_enthalpy(Pressure=1.01325, molecule_name=name)

col1, col2, col3, col4 = st.columns(4)

st.write(f"The boiling point of {name} at {pres} [bar] is:  ")

with col1:
    st.metric("", round(bp,2), delta=round(bp-bpatm, 2), label_visibility="collapsed")
with col2:
    st.subheader("[K]")
with col3:
    st.metric("", round(bp-273.15,2), delta=round(bp-bpatm, 2), label_visibility="collapsed")
with col4:
    st.subheader("[°C]")

#st.header(f"{bp:.2f} [K] or {bp-273.15:.2f} [°C]")

st.write("Comparaison with the boiling point at atmospheric pressure in Kelvin and Celsius:")

#with col1:
    #st.metric("",value=round(bpatm, 2), delta=round(bp-bpatm, 2), label_visibility="collapsed")
#with col2:
    #st.subheader("[K]")
#with col3:
    #st.metric("",value=round(bpatm-273.15,2), delta=round(bp-bpatm, 2), label_visibility="collapsed")
#with col4:
    #st.subheader("[°C]")
