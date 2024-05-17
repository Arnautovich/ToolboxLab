import numpy as np


def clausius_clapeyron (T,P): 
    
    return 1/((1/T)-(np.log(P/1.01325)*R/(T*(4.4+np.log(T)))))


import chemicals 
def clausius_clapeyron_enthalpy (Pressure,CASRN):
#P in bar
# T in K
    
   
    Liquid_heat_compound = chemicals.reaction.Hfl(CASRN, method=None)
    
    Gas_heat_compound = chemicals.reaction.Hfg(CASRN, method=None)
    
    T = chemicals.phase_change.Tb(CASRN, method=None)
    
    latent_heat_compound = Gas_heat_compound - Liquid_heat_compound
    
    New_Boiling_Point_at_P = 1/((1/T)-(np.log(Pressure/1.01325)*8.314/(latent_heat_compound)))
