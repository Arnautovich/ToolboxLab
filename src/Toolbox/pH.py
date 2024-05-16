import numpy as np

def bufferpH (ca:float=1, cb:float=1, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the pH of a buffer solution of a weak acid/base couple, knowing the concentrations of compounds and either the pKa, Ka or Kb

    input : 
    ca: The concentration of acid [AH]
    cb: The concentration of the conjugate base [A-]
    pka: The pKa of the couple
    *
    Ka: Can be used instead of the pka, the acidity constant of the couple
    Kb: Can be used instead of the pka, The basicity constant of the couple 

    output:
    pH as float
    '''

    if pka == None and Ka != None:
        pka = -np.log10(Ka)
    else:
        pka = -np.log10(1*10**(-14)/Kb)

    return float(pka + np.log10(cb/ca))


def bufferconc (pH:float=7, ca:float=None, cb:float=None, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the concentration of one compound in a buffer solution of a weak acid/base couple, knowing the pH and the concentration of the conjugate compound

    input:
    pH: of the buffer solution
    ca: The concentration of acid [HA]
    cb: The concentration of base [A-]
    pka: The pKa of the couple
    *
    Ka: Can be used instead of the pka, the acidity constant of the couple
    Kb: Can be used instead of the pka, the basicity constant of the couple

    output:
    The missing concentration as float
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


def strongacidpH (ca:float) -> float:
    '''
    This function calculates the pH of a strong acid in water

    input:
    ca: The concentration of acid [HA]

    output:
    The pH of the solution as float
    '''
    return -np.log10(0.5*ca + np.sqrt(0.25*ca**2 + 10**(-14)))


def strongbasepH (cb:float) -> float:
    '''
    This function calculates the pH of a strong base in water

    input:
    cb: The concentration of base [B-]

    output:
    The pH of the solution as float
    '''
    return -np.log10(-0.5*cb + np.sqrt(0.25*cb**2 + 10**(-14)))


def strongacidconc (pH:float) -> float:
    '''
    
    '''
    return 10**(-pH)-10**(-7)


def strongbaseconc (pH:float=None, pOH:float=None) -> float:
    '''
    
    '''

    if pOH != None and pH == None:
        pH = 14 - pOH

    return 10**(pH-14) - 10**(-7-pH)


def weakacidpH (ca:float, Ka:float=None, pka:float=None) -> float:
    '''
    This function calculates the pH of a weak acid in water

    input:
    ca: The concentration of acid [HA]
    Ka: The acidity constant of the acid
    *
    pka: Can be used instead of Ka, the pKa of the acid

    output:
    The pH of the solution as a float
    '''
    if pka != None and Ka == None:
        Ka = 10**(-pka)

    if ca > 10**(-7):
        return -np.log10(-0.5*Ka + np.sqrt(0.25*Ka**2 + ca*Ka))
    else:
        raise "the concentration is too low to calculate precisely"

    
def weakbasepH (cb:float, Ka:float=None, pka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the pH of a weak base in water

    input:
    cb: The concentration of base [B-]
    Ka: The acidity constant of the base 
    *
    pka: Can be used instead of Ka, the pKa of the base 
    Kb: Can be used instead of Ka, the basicity constant of the base

    output:
    The pH of the solution as a float
    '''

    if pka != None and Ka == None and Kb == None:
        Ka = 10**(-pka)
    elif Kb != None and Ka == None and pka == None:
        Ka = 10**(-14)/Kb
    
    if cb > 10**(-7):
        return float(-np.log10(0.5*10**(-14)/cb + np.sqrt(0.25*(10**(-14)/cb)**2 + 10**(-14)*Ka/cb)))
    else:
        raise "Concentration too low to calculate precisely"


def weakacidconc (pH:float, Ka:float=None, pka:float=None) -> float:
    '''
    
    '''

    if pka != None and Ka == None:
        Ka = 10**(-pka)

    return (10**(-pH)*(10**(-pH)+Ka))/Ka, ((10**(-pH)-10**(-7))*(10**(-pH)+Ka))/Ka


def weakbaseconc (pH:float, Kb:float=None, pka:float=None, Ka:float=None):
    '''

    '''

    if pka != None and Kb == None and Ka == None:
        Kb = 10**(pka-14)
    elif Ka != None and Kb == None and pka == None:
        Kb = 10**(-7)/Ka
    
    cOH = 10**(-14)/10**(-pH)

    return (cOH-10**(-7))/Kb*(cOH + Kb)


# pKa < -2 => strong acid 
# modifier descriptions buffer 
# faire plus de test mais normalement c'est correcte 


if __name__ == "__main__" :
    #print("pH buffer :", bufferpH(0.4, 1, Kb=1.8*10**(-5)))
    #print("concentration buffer :", bufferconc(9.65, 0.4, None, Kb=1.8*10**(-5)))
    print("pH acide fort :",strongacidpH(0.234))
    print("pH base forte :",strongbasepH(2*0.013))
    print("conc acide fort :", strongacidconc(0.6307))
    print("conc base forte :", strongbaseconc(12.41497))
    #print("pH acide faible :", weakacidpH(0.2, Ka=1.74*10**(-5)))
    #print("pH base faible :", weakbasepH(0.5*10**(-6), 10**(-6)))
    #print("conc d'acide faible :", weakacidconc(3.11, 6.5*10**(-5)))
    #print("conc de base faible :", weakbaseconc(11.13, Kb=1.77*10**(-5)))