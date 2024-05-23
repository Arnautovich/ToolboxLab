import streamlit as st
import Toolbox.pH as tp

st.header("What do you want to calculate :")

col1, col2 = st.columns(2)

with col1:

    comp = st.radio("Which compound do you need ?", ["Strong acid", "Strong base", "Weak acid", "Weak base", "Buffer solution"], index=None)

with col2:

    val = st.radio("Which value do you need ?", ["pH", "Concentration"], index=None)

if comp == "Strong acid" and val == "pH":
    conc = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5))
    pH = tp.strongacidpH(conc)
    st.write(f"The pH calculated is {pH}")

elif comp == "Strong acid" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5))
    conc = tp.strongacidconc(pH)
    st.write(f"The concentration calculated is {conc} [mol/L]")

elif comp == "Strong base" and val == "pH":
    conc = st.number_input("The concentration of your base [mol/L]:", 0.0, step= 10**(-5))
    pH = tp.strongbasepH(conc)
    st.write(f"The pH calculated is {pH}")

elif comp == "Strong base" and val == "Concentration":
    sel = st.selectbox("which scale are you using ?", ["pH", "pOH"])

    pH, pOH = None, None

    if sel == "pH":
        pH = st.number_input("The pH of your solution:", step=10**(-5))
    else:
        pOH = st.number_input("The pOH of your solution:", step=10**(-5))
    
    conc = tp.strongbaseconc(pH=pH, pOH=pOH)
    st.write(f"The concentration calculated is {conc} [mol/L]")

elif comp == "Weak acid" and val == "pH":
    conc = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5))
    sel = st.selectbox("Which constant are you using ?", ["Ka","pKa"])

    ka, pka = None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your acid:", step=10**(-14))
    else:
        pka = st.number_input("The pKa of your acid:", step=10**(-14))
    
    pH = tp.weakacidpH(conc, Ka=ka, pka=pka)

    st.write(f"The pH calculated is {pH}")

elif comp == "Weak acid" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5))
    sel = st.selectbox("Which constant are you using ?", ["Ka", "pKa"])

    ka, pka = None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your acid:", step=10**(-14))
    else:
        pka = st.number_input("The pKa of your acid:", step=10**(-14))
    
    conc = tp.weakacidconc(pH, Ka=ka, pka=pka)

    st.write(f"The concentration of your acid is {conc} [mol/L]")

elif comp == "Weak base" and val == "pH":
    conc = st.number_input("The concentration of your base [mol/L]:", 0.0, step= 10**(-5))
    sel = st.selectbox("Which constant are you using ?", ["Ka", "pKa", "Kb"])

    ka, pka, kb = None, None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your base:", step=10**(-14))
    elif sel == "pKa":
        pka = st.number_input("The pKa of your base:", step=10**(-5))
    else:
        kb = st.number_input("The Kb of your base:", step=10**(-14))
    
    pH = tp.weakbasepH(conc, Ka=ka, pka=pka, Kb=kb)

    st.write(f"The pH calculated is {pH}")

elif comp == "Weak base" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5))
    sel = st.selectbox("Which constant are you using ?", ["Kb", "pKa", "Ka"])

    kb, pka, ka = None, None, None

    if sel == "Kb":
        kb = st.number_input("The Kb of your base:", step=10**(-14))
    elif sel == "pKa":
        pka = st.number_input("The pKa of your base:", step=10**(-5))
    else:
        ka = st.number_input("The Ka of your base:", step=10**(-14))

    conc = tp.weakbaseconc(pH, Kb=kb, pka=pka, Ka=ka)

    st.write(f"The concentration of your base is {conc}")

elif comp == "Buffer solution" and val =="pH":
    ca = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5))
    cb = st.number_input("The concentration of your base [mol/L]:", 0.0, step=10**(-5))
    sel = st.selectbox("Which constant are you using ?", ["pKa", "Ka", "Kb"])
    
    pka, ka, kb = None, None, None

    if sel == "pKa":
        pka = st.number_input("The pKa of your couple acid/base:", step=10**(-5))
    elif sel == "Ka":
        ka = st.number_input("The Ka of your couple acid/base:", step=10**(-14))
    else:
        kb = st.number_input("The Kb of your couple acid/base:", step=10**(-14))
    
    pH = tp.bufferpH(ca=ca, cb=cb, pka=pka, Ka=ka, Kb=kb)

    st.write(f"The pH calculated is {pH}")

elif comp == "Buffer solution" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5))
    sel1 = st.selectbox("Which concentration are you missing ?", ["Concentration of acid", "Concentration of base"])
    if sel1 == "Concentration of acid":
        ca = st.number_input("The concentration of your acid:", step=10**(-5))
    elif sel1 == "Concentration of base":
        cb = st.number_input("The concentration of your base:", step=10**(-5))

    sel2 = st.selectbox("Which constant are you using ?", ["pKa", "Ka", "Kb"])

    pka, ka, kb = None, None, None

    if sel2 == "pKa":
        pka = st.number_input("The pKa of your couple acid/base:", step=10**(-5))
    elif sel2 == "Ka":
        ka = st.number_input("The Ka of your couple acid/base:", step=10**(-14))
    else:
        kb = st.number_input("The Kb of your couple acid/base:", step=10**(-14))
    
    conc = tp.bufferconc(pH=pH, ca=ca, cb=cb, pka=pka, Ka=ka, Kb=kb)

    st.write(f"The missing concentration of the couple acid/base is {conc}")
