import streamlit as st
import Toolbox.pH as tp

st.header("pH Calculator")

st.write("What do you want to calculate ?")

col1, col2 = st.columns(2)

with col1:

    comp = st.radio("Which compound do you use ?", ["Strong acid", "Strong base", "Weak acid", "Weak base", "Buffer solution"], index=None)

with col2:

    val = st.radio("Which value do you need ?", ["pH", "Concentration"], index=None)

if comp == "Strong acid" and val == "pH":
    conc = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5), value=None)
    pH = tp.strongacidpH(conc)
    st.subheader(f"The pH calculated is {pH}")

elif comp == "Strong acid" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5), value=None)
    conc = tp.strongacidconc(pH)
    st.subheader(f"The concentration calculated is {conc} [mol/L]")

elif comp == "Strong base" and val == "pH":
    conc = st.number_input("The concentration of your base [mol/L]:", 0.0, step= 10**(-5), value=None)
    pH = tp.strongbasepH(conc)
    st.subheader(f"The pH calculated is {pH}")

elif comp == "Strong base" and val == "Concentration":
    sel = st.selectbox("which scale are you using ?", ["pH", "pOH"])

    pH, pOH = None, None

    if sel == "pH":
        pH = st.number_input("The pH of your solution:", step=10**(-5), value=None)
    else:
        pOH = st.number_input("The pOH of your solution:", step=10**(-5), value=None)
    
    conc = tp.strongbaseconc(pH=pH, pOH=pOH)
    st.subheader(f"The concentration calculated is {conc} [mol/L]")

elif comp == "Weak acid" and val == "pH":
    conc = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5), value=None)
    sel = st.selectbox("Which constant are you using ?", ["Ka","pKa"])

    ka, pka = None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your acid:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    else:
        pka = st.number_input("The pKa of your acid:", step=10**(-14), value=None)
    
    pH = tp.weakacidpH(conc, Ka=ka, pka=pka)

    st.subheader(f"The pH calculated is {pH}")

elif comp == "Weak acid" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5), value=None)
    sel = st.selectbox("Which constant are you using ?", ["Ka", "pKa"])

    ka, pka = None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your acid:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    else:
        pka = st.number_input("The pKa of your acid:", step=10**(-14), value=None)
    
    conc = tp.weakacidconc(pH, Ka=ka, pka=pka)

    st.subheader(f"The concentration of your acid is {conc} [mol/L]")

elif comp == "Weak base" and val == "pH":
    conc = st.number_input("The concentration of your base [mol/L]:", 0.0, step= 10**(-5), value=None)
    sel = st.selectbox("Which constant are you using ?", ["Ka", "pKa", "Kb"])

    ka, pka, kb = None, None, None

    if sel == "Ka":
        ka = st.number_input("The Ka of your base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    elif sel == "pKa":
        pka = st.number_input("The pKa of your base:", step=10**(-5), value=None)
    else:
        kb = st.number_input("The Kb of your base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    
    pH = tp.weakbasepH(conc, Ka=ka, pka=pka, Kb=kb)

    st.subheader(f"The pH calculated is {pH}")

elif comp == "Weak base" and val == "Concentration":
    pH = st.number_input("The pH of your solution:", step=10**(-5), value=None)
    sel = st.selectbox("Which constant are you using ?", ["Kb", "pKa", "Ka"])

    kb, pka, ka = None, None, None

    if sel == "Kb":
        kb = st.number_input("The Kb of your base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    elif sel == "pKa":
        pka = st.number_input("The pKa of your base:", step=10**(-5), value=None)
    else:
        ka = st.number_input("The Ka of your base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")

    conc = tp.weakbaseconc(pH, Kb=kb, pka=pka, Ka=ka)

    st.subheader(f"The concentration of your base is {conc}")

elif comp == "Buffer solution" and val =="pH":
    ca = st.number_input("The concentration of your acid [mol/L]:", 0.0, step= 10**(-5), value=None)
    cb = st.number_input("The concentration of your base [mol/L]:", 0.0, step=10**(-5), value=None)
    sel = st.selectbox("Which constant are you using ?", ["pKa", "Ka", "Kb"])
    
    pka, ka, kb = None, None, None

    if sel == "pKa":
        pka = st.number_input("The pKa of your couple acid/base:", step=10**(-5), value=None)
        pH = tp.bufferpH(ca=ca, cb=cb, pka=pka)
    elif sel == "Ka":
        ka = st.number_input("The Ka of your couple acid/base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
        pH = tp.bufferpH(ca=ca, cb=cb, Ka=ka)
    else:
        kb = st.number_input("The Kb of your couple acid/base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
        pH = tp.bufferpH(ca=ca, cb=cb, Kb=kb)
    
    st.subheader(f"The pH calculated is {pH:.2f}")

elif comp == "Buffer solution" and val == "Concentration":
    ca, cb = None, None
    pH = st.number_input("The pH of your solution:", step=10**(-5), value=None)
    sel1 = st.selectbox("Which concentration are you missing ?", ["Concentration of acid", "Concentration of base"])
    if sel1 == "Concentration of acid":
        ca = st.number_input("The concentration of your base:", step=10**(-5), value=None)
    elif sel1 == "Concentration of base":
        cb = st.number_input("The concentration of your acid:", step=10**(-5), value=None)

    sel2 = st.selectbox("Which constant are you using ?", ["pKa", "Ka", "Kb"])

    pka, ka, kb = None, None, None

    if sel2 == "pKa":
        pka = st.number_input("The pKa of your couple acid/base:", step=10**(-5), value=None)
    elif sel2 == "Ka":
        ka = st.number_input("The Ka of your couple acid/base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    else:
        kb = st.number_input("The Kb of your couple acid/base:", step=10**(-14), value=None, help="You can use this notation for power of 10 : xey = x*10^y")
    
    conc = tp.bufferconc(pH=pH, ca=ca, cb=cb, pka=pka, Ka=ka, Kb=kb)

    st.write(f"You have choosen to calculate the missing {sel1} in a buffer solution with a pH of {pH} and a {sel2} of {pka if pka is not None else ka if ka is not None else kb if kb is not None else None}")
    st.subheader(f"The missing {sel1} is {conc:.3f} mol/L")
