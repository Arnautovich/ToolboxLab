import streamlit as st
import Toolbox.Pressure_TB as tp

st.header("Boiling Point at new Pressure")

pres = st.number_input("The pressure of the operation in [bar]:", 0.001, value=None, step=0.001)
name = st.text_input("The name of the molecule:", value=None, help="If the molecule does not work, try different names. If it still doesn't work maybe this molecule is not supported by the package: Chemicals")

if pres is not None and name is not None and name != '':
    bp = tp.clausius_clapeyron_enthalpy(Pressure=pres, molecule_name=name)
    bpatm = tp.clausius_clapeyron_enthalpy(Pressure=1.01325, molecule_name=name)

    col1, col2, col3, col4 = st.columns(4)

    st.write(f"The boiling point of {name} at {pres} [bar] is:   ")
    st.write("The values bellow are a comparaison with the boiling point at atmospheric pressure in Kelvin and Celsius:")

    with col1:
        st.metric("", round(bp,2), delta=round(bp-bpatm, 2), label_visibility="hidden")
    with col2:
        st.subheader("[K]")
    with col3:
        st.metric("", round(bp-273.15,2), delta=round(bp-bpatm, 2), label_visibility="collapsed")
    with col4:
        st.subheader("[°C]")

else:
    st.write("Please enter the pressure and the name of the molecule")

# mettre texte avant le metric 