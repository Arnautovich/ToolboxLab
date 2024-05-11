import numpy as np

def pHfromconc (ca:float=1, cb:float=1, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the pH of a weak acid/base solution knowing the concentrations of compounds and either the pKa, Ka or Kb

    input : 
    ca: The concentration of acid [AH]
    cb: The concentration of the conjugate base [A-]
    pka: The pKa of the couple
    *
    Ka: The acidity constant of the couple
    Kb: The basicity constant of the couple 

    output:
    pH as float
    '''

    if pka == None and Ka != None:
        pka = -np.log10(Ka)
    else:
        pka = -np.log10(1*10**(-14)/Kb)

    return float(pka + np.log10(cb/ca))


def concfrompH (pH:float=7, ca:float=None, cb:float=None, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the concentration of a weak acid/base knowing the pH and the concentration of its conjugate

    input:
    pH
    ca: The concentration of acid [HA]
    cb: The concentration of base [A-]
    pka: The pKa of the couple
    *
    Ka: The acidity constant of the couple
    Kb: The basicity constant of the couple

    output:
    The concentration missing as float
    '''

    if pka == None and Ka != None:
        pka = -np.log10(Ka)
    else:
        pka = -np.log10(1*10**(-14)/Kb)

    if ca == None:
        ca = cb/(10**(pH-pka))
        return float(ca)
    else:
        cb = ca*10**(pH-pka)
        return float(cb)

def strongacid (ca:float) -> float:
    '''
    This function calculates the pH of a strong acid in water
    '''
    return -np.log10(0.5*ca + np.sqrt(0.25*ca**2 + 10**(-14)))

def strongbase (cb:float) -> float:
    '''
    
    '''
    return -np.log10(-0.5*cb + np.sqrt(0.25*cb**2 + 10**(-14)))


# changer deux première fonction par buffer 
print("le pH est : ", pHfromconc(0.4, 1, Kb=1.8*10**(-5)))
print("la concentration est :", concfrompH(9.65, 0.4, None, Kb=1.8*10**(-5)))
print(strongacid(0.234))
print(strongbase(2*0.013))