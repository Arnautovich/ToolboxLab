import numpy as np

def bufferpH (ca:float, cb:float, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the pH of a buffer solution of a weak acid/base couple in water, 
    by knowing the concentrations of compounds and either the pKa, Ka or Kb

    input : 
    ca: The concentration of acid [AH] (mol/L)
    cb: The concentration of the conjugate base [A-] (mol/L)
    pka: The pKa of the couple
    *
    Ka: Can be used instead of the pka, the acidity constant of the couple
    Kb: Can be used instead of the pka, The basicity constant of the couple 

    output:
    pH as float
    '''

    if ca <0 or cb <0:
        raise ValueError("The concentration can not be negative")
    elif pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif Ka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None and Kb is None:
        raise Exception("At least one constant must be given")


    if pka is None and Ka is not None:
        if Ka <=0:
            raise ValueError("The constant can not be negative or equal to 0")
        pka = -np.log10(Ka)
    elif pka is None and Kb is not None:
        if Kb <=0:
            raise ValueError("The constant can not be negative or equal to 0")
        pka = -np.log10(1*10**(-14)/Kb)
    
    return float(pka + np.log10(cb/ca))


def bufferconc (pH:float, ca:float=None, cb:float=None, pka:float=None, Ka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the concentration of one compound, in a buffer solution of a weak acid/base couple in water, needed to achieve the pH indicated
    by knowing the pH, the concentration of the conjugate compound and either the pKa, Ka or Kb

    input:
    pH of the buffer solution
    ca: The concentration of acid [HA] (mol/L)
    cb: The concentration of base [A-] (mol/L)
    pka: The pKa of the couple
    *
    Ka: Can be used instead of the pka, the acidity constant of the couple
    Kb: Can be used instead of the pka, the basicity constant of the couple

    output:
    The missing concentration (mol/L) as float
    '''
    # Check the input
    if ca is not None and ca < 0:
        raise ValueError("The concentration can not be negative")
    elif cb is not None and cb < 0:
        raise ValueError("The concentration can not be negative")
    elif pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif Ka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None and Kb is None:
        raise Exception("At least one constant must be given")

    # Calculate pKa if Ka or Kb given
    if pka is None:
        if Ka is not None:
            if Ka <= 0:
                raise ValueError("The acidity constant (Ka) must be positive")
            pka = -np.log10(Ka)
        elif Kb is not None:
            if Kb <= 0:
                raise ValueError("The basicity constant (Kb) must be positive")
            pka = 14 + np.log10(Kb)

    # Calculate the missing concentration
    if ca is None and cb is not None:
        ca = cb / (10**(pH - pka))
        if ca < 0:
            raise ValueError("The concentration calculated is negative, check your inputs")
        return float(ca)
    
    elif cb is None and ca is not None:
        cb = ca * (10**(pH - pka))
        if cb < 0:
            raise ValueError("The concentration calculated is negative, check your inputs")
        return float(cb)
    else:
        raise ValueError("Exactly one of ca or cb must be provided")


def strongacidpH (ca:float) -> float:
    '''
    This function calculates the pH of a strong acid (pKa <= -1) in water

    input:
    ca: The concentration of acid [HA] (mol/L)

    output:
    The pH of the solution as float
    '''
    if ca <0:
        raise ValueError("The concentration calculated is negative, check your inputs")

    return float(-np.log10(0.5*ca + np.sqrt(0.25*ca**2 + 10**(-14))))


def strongbasepH (cb:float) -> float:
    '''
    This function calculates the pH of a strong base (pKa <= -1) in water

    input:
    cb: The concentration of base [B-] (mol/L)

    output:
    The pH of the solution as float
    '''
    if cb <0:
        raise ValueError("The concentration calculated is negative, check your inputs")

    return -np.log10(-0.5*cb + np.sqrt(0.25*cb**2 + 10**(-14)))


def strongacidconc (pH:float) -> float:
    '''
    This function calculates the concentration of strong acid (pKa <= -1) needed to achieve the pH indicated, in water

    input:
    pH wanted in the solution

    output:
    The concentration of strong acid needed (mol/L) as float
    '''
    ca =  float(10**(-pH)-10**(-7))
    if ca <0:
        raise ValueError("The concentration calculated is negative, check your inputs")
    return ca


def strongbaseconc (pH:float=None, pOH:float=None) -> float:
    '''
    This function calculates the concentration of strong base (pKa >= 14) needed to achieve the pH indicated, in water

    input:
    pH wanted
    *
    pOH: Can be used instead of pH, the potential of hydroxide wanted

    output:
    The concentration of strong base needed (mol/L) as float
    '''

    if pOH is not None and pH is None:
        pH = 14 - pOH
    
    cb = float(10**(pH-14) - 10**(-7-pH))
    if cb <0:
        raise ValueError("The concentration calculated is negative, check your inputs")
    return cb


def weakacidpH (ca:float, Ka:float=None, pka:float=None) -> float:
    '''
    This function calculates the pH of weak acid in water, 
    by knowing the concentration of the acid and either its Ka or pKa

    input:
    ca: The concentration of acid [HA] (mol/L)
    Ka: The acidity constant of the acid \n
    *
    pka: Can be used instead of Ka, the pKa of the acid

    output:
    The pH of the solution as a float
    '''
    if ca <0:
        raise ValueError("The concentration can not be negative")
    elif pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None:
        raise Exception("At least one constant must be given")


    if pka is not None and Ka is None:
        Ka = 10**(-pka)

    if ca > 10**(-7):
        return float(-np.log10(-0.5*Ka + np.sqrt(0.25*Ka**2 + ca*Ka)))
    else:
        raise ValueError("Concentration too low to calculate precisely")

    
def weakbasepH (cb:float, Ka:float=None, pka:float=None, Kb:float=None) -> float:
    '''
    This function calculates the pH of a weak base in water,
    by knowing the concentration of base and either its Ka, pKa or Kb

    input:
    cb: The concentration of base [B-] (mol/L)
    Ka: The acidity constant of the base 
    *
    pka: Can be used instead of Ka, the pKa of the base 
    Kb: Can be used instead of Ka, the basicity constant of the base

    output:
    The pH of the solution as a float
    '''
    if cb <0:
        raise ValueError("The concentration can not be negative")
    elif pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif Ka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None and Kb is None:
        raise Exception("At least one constant must be given")


    if pka is not None and Ka is None and Kb is None:
        Ka = 10**(-pka)
    elif Kb is not None and Ka is None and pka is None:
        if Kb <0:
            raise ValueError()
        Ka = 10**(-14)/Kb
    
    if cb > 10**(-7):
        return float(-np.log10(0.5*10**(-14)/cb + np.sqrt(0.25*(10**(-14)/cb)**2 + 10**(-14)*Ka/cb)))
    else:
        raise ValueError("Concentration too low to calculate precisely")


def weakacidconc (pH:float, Ka:float=None, pka:float=None) -> float:
    '''
    This function calculates the concentration of weak acid needed to achieve the pH desired in water,
    by knowing the pH and either the Ka or pKa 

    input:
    pH of the solution
    Ka: The acidity constant of the compound
    *
    pka: Can be used instead of the Ka, the pKa of the compound

    output:
    The concentration of weak acid needed (mol/L) as a float
    '''
    if pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None:
        raise Exception("At least one constant must be given")


    if pka is not None and Ka is None:
        Ka = 10**(-pka)

    ca = float(((10**(-pH)-10**(-7))*(10**(-pH)+Ka))/Ka)
    if ca <0:
        raise ValueError("The concentration calculated is negative, check your inputs")

    return ca 


def weakbaseconc (pH:float, Kb:float=None, pka:float=None, Ka:float=None) -> float:
    '''
    This function calculates the concentration of weak base needed to achieve the pH desired in water,
    by knowing the pH and either the Kb, pKa or Ka

    input:
    pH of the solution
    Kb: The basicity constant of the compound 
    *
    pka: Can be used instead of the Kb, the pKa of the compound
    Ka: Can be used instead of the Kb, the acidity constant of the compound

    output:
    The concentration of weak base needed (mol/L) as a float
    '''
    if pka is not None and Ka is not None:
        raise Exception("Only one constant can be input")
    elif pka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif Ka is not None and Kb is not None:
        raise Exception("Only one constant can be input")
    elif pka is None and Ka is None and Kb is None:
        raise Exception("At least one constant must be given")


    if pka is not None and Kb is None and Ka is None:
        Kb = 10**(pka-14)
    elif Ka is not None and Kb is None and pka is None:
        Kb = 10**(-14)/Ka
    
    cOH = 10**(-14)/10**(-pH)

    cb = float((cOH-10**(-7))/Kb*(cOH + Kb))
    if cb <0:
        raise ValueError("The concentration calculated is negative, check your inputs")

    return cb


if __name__ == "__main__" :
    print("Value :", weakbaseconc(12, Ka=10**-10))