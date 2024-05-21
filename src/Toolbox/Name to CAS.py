import requests
import numpy as np
def resolve_name_to_cas(molecule_name):
    
        # Construct the URL for the CIR service
    url = f"https://commonchemistry.cas.org/results?q={molecule_name}"

        # Send a GET request to the CIR service
    response = requests.get(url)

    find = "Result: "
    start=response.text.find(find)+len(find)
    end = response.text.find("," ,start)
    return response.text[start: end]
    