import numpy as np

def pHfromconc (ca:float=1, cb:float=1, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    
    '''
    if pka == None and Ka != None:
        pka = -np.log10(K)
    else:
        pka = -np.log10(1*10**(-14)/Kb)

    return pka + np.log10(cb/ca)

def concfrompH (pH:float=7, ca:float=None, cb:float=None, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    Define one concentration to calculate the second
    '''

    if pka == None and Ka != None:
        pka = -np.log10(K)
    else:
        pka = -np.log10(1*10**(-14)/Kb)

    if ca == None:
        ca = cb/(10**(pH-pka))
        return ca
    else:
        cb = ca*10**(pH-pka)
        return cb



print("le pH est : ", pHfromconc(0.4, 1, Kb=1.8*10**(-5)))
print("la concentration est :", concfrompH(9.65, 0.4, None, Kb=1.8*10**(-5)))
