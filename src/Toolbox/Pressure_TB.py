
import requests
import numpy as np
import chemicals 

def resolve_name_to_cas(molecule_name):
    
        # Construct the URL for the CIR service
    url = f"https://commonchemistry.cas.org/results?q={molecule_name}"

        # Send a GET request to the CIR service
    response = requests.get(url)

    find = "Result: "
    start=response.text.find(find)+len(find)
    end = response.text.find("," ,start)
    return response.text[start: end]

    


<<<<<<< HEAD

import chemicals 
def clausius_clapeyron_enthalpy (Pressure,molecule_name):
=======
def clausius_clapeyron_enthalpy (Pressure,STR):
>>>>>>> 1b1d6960a3f08d5e6af7389598059a2d7b83a262
#P in bar
# T in K
    CASRN = resolve_name_to_cas(molecule_name)
   
    Liquid_heat_compound = chemicals.reaction.Hfl(CASRN, method=None)
    
    Gas_heat_compound = chemicals.reaction.Hfg(CASRN, method=None)
    
    T = chemicals.phase_change.Tb(CASRN, method=None)
    
    latent_heat_compound = Gas_heat_compound - Liquid_heat_compound
    
    New_Boiling_Point_at_P = 1/((1/T)-(np.log(Pressure/1.01325)*8.314/(latent_heat_compound)))

    return New_Boiling_Point_at_P
