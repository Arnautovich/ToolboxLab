import streamlit as st
import Toolbox.Solvent as ts 
import pandas as pd

st.header("Solvent Determination")

reaction_list = ["SN1","SN2","Aldol",
                 "Esterification","Grignard",
                 "Friedel-Crafts","Hydrogenation",
                 "Oxidation","Reduction",
                 "Heck","Suzuki Coupling",
                 "Sonogashira Coupling","Nitration",
                 "Sulfonation","Amination",
                 "Michael Addition","Fischer Esterification",
                 "Buchwald-Hartwig Amination","Grignard addition",
                 "Wittig Reaction","Claisen Condensation",
                 "Cannizzaro Reaction","Baeyer-Villiger Oxidation",
                 "Polymerization","Crystallization Reactions",
                 "Enzymatic Reactions","Phase Transfer Catalysis",
                 "Reflux Reactions","Distillation",
                 "Knoevenagel Condensation","Recrystallization",
                 "Steam Distillation"]

reaction_picked = st.selectbox("What type of **reaction** are you doing ?", reaction_list, index=None)
boiling_point = st.number_input("The targeted **boiling point** of your solvent [°C]:", value=None)
polarity = st.number_input("The targeted **polarity** (by Snyder) of your solvent:", value=None)
viscosity = st.number_input("The targeted **viscosity** of your solvent [mPa $\cdot$ s]:", value=None)

if reaction_picked != None and boiling_point != None and polarity != None and viscosity != None:

    result = ts.select_solvent(reaction_type=reaction_picked, boiling_point=boiling_point, polarity=polarity, viscosity=viscosity)

    datab = pd.DataFrame(result, index=[1,2,3,4,5], columns=["Name", "Score"])

    st.write(f"The 5 best solvents for {reaction_picked} reaction are :")
    st.dataframe(datab)
    st.write("The 'Score' column uses an arbitrary unit to classify coumpounds  ")
    st.write('''The solvents are picked from this list :  
- Water  
- Ethanol  
- Diethyl ether  
- Pentane  
- 1,1,2-Trichlorotrifluoroethane  
- Cyclopentane  
- Heptane  
- Hexane  
- Iso-Octane  
- Petroleum Ether  
- Cyclohexane  
- n-Butyl Chloride  
- Toluene  
- Methyl t-Butyl Ether  
- o-Xylene  
- Chlorobenzene  
- o-Dichlorobenzene  
- Ethyl Ether  
- Dichloromethane  
- Ethylene Dichloride  
- n-Butyl Alcohol  
- Isopropyl Alcohol  
- n-Butyl Acetate  
- Isobutyl Alcohol  
- Methyl Isoamyl Ketone  
- n-Propyl Alcohol  
- Tetrahydrofuran  
- Chloroform  
- Methyl Isobutyl Ketone  
- Ethyl Acetate  
- Methyl n-Propyl Ketone  
- Methyl Ethyl Ketone  
- 1,4-Dioxane  
- Methanol  
- Acetone  
- Pyridine  
- 2-Methoxyethanol  
- Acetonitrile  
- Propylene Carbonate  
- N,N-Dimethylformamide  
- Dimethyl Acetamide  
- N-Methylpyrrolidone  
- Dimethyl Sulfoxide
             ''')
else:
    st.write("Please enter your values")