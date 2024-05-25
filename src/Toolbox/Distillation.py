import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from typing import Iterable, Union

def ahline(ax:object, y:float, xmin:float, xmax:float) -> None:
    '''
    This function draws a horizontal line on the plot. The input parameters are:
    ax: the axis object
    y: the y-coordinate of the horizontal line
    xmin: the starting x-coordinate of the line
    xmax: the ending x-coordinate of the line
    '''
    ax.axhline(y=y,xmin=xmin, xmax=xmax, linestyle='--', color='black', dash_capstyle='round')

def avline(ax:object, x:float, ymin:float, ymax:float) -> None:
    '''
    This function draws a vertical line on the plot. The input parameters are:
    ax: the axis object
    x: the x-coordinate of the vertical line
    ymin: the starting y-coordinate of the line
    ymax: the ending y-coordinate of the line
    '''
    ax.axvline(x=x,ymin=ymin, ymax=ymax, linestyle='--', color='black', dash_capstyle='round')

def equilibrium_line(alpha:float, x:Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    '''
    This function calculates the equilibrium value of x given alpha. The input parameters are:
    alpha: Relative volatility of the light component with respect to the heavy component
    x: a float or an array of floats representing the points at which the equilibrium value of x is to be calculated
    '''
    return alpha*x/(1-x+alpha*x)

def x_label(ax:object, x:float, text:str) -> None:
    '''
    This function adds a label to the x-axis. The input parameters are:
    ax: the axis object
    x: the x-coordinate of the label
    text: the text of the label
    '''
    ax.annotate(text, xy=(x,0), xytext=(x+0.01, 0.02), fontsize=10, color='black',fontname='Arial')

def y_label(ax:object, y:float, text:str) -> None:
    '''
    This function adds a label to the y-axis. The input parameters are:
    ax: the axis object
    y: the y-coordinate of the label
    text: the text of the label
    '''
    ax.annotate(text, xy=(0.01,y+0.02), xytext=(0.01, y+0.02), fontsize=10, color='black',fontname='Arial')

def enriching_operating_line(R:float, x:Union[np.ndarray, float], xD:float) -> Union[np.ndarray, float]:
    '''
    This function calculates the enriching operating line. The input parameters are:
    R: the reflux ratio
    x: a float or an array of floats representing the points at which the enriching operating line is to be calculated
    xD: the distillate composition
    '''
    return R/(R+1)* x + 1/(R+1)*xD

def stripping_operating_line(R:float, xB:float, xD:float, x_inter:float, x:Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    '''
    This function calculates the stripping operating line. The input parameters are:
    R: the reflux ratio
    xB: the bottom composition
    xD: the distillate composition
    x_inter: the x-coordinate of the intersection of the feed line and enriching operating lines
    x: a float or an array of floats representing the points at which the stripping operating line is to be calculated
    '''
    y_inter = enriching_operating_line(R, x_inter, xD)
    yB = xB

    slope = (y_inter - yB)/(x_inter - xB)
    intercept = yB - slope * xB

    return slope*x + intercept

def feed_line(q:float,z:float,x:Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    '''
    This function calculates the feed line. The input parameters are:
    q: feed quality
    z: the feed composition of the light component
    x: a float or an array of floats representing the points at which the feed line is to be calculated
    '''
    if q == 1:
        q = 1.000000001
        
    return -q/(1-q)*x + z/(1-q)

def distillation(xD:float, R:float, z:float, q:float, alpha:float, xB:float=None, D:float = None, F:float=None) -> int:
    '''
    This function plots the McCabe-Thiele diagram for a binary distillation column. The inputs are the following:
    
    xD: Mole fraction of the light component in the distillate
    R: Reflux ratio
    z: Mole fraction of the light component in the feed
    q: Feed quality
    alpha: Relative volatility of the light component with respect to the heavy component
    xB: Mole fraction of the light component in the bottoms
    D: Distillate flow rate
    F: Total flow rate of the feed

    The function returns the number of stages required for the separation and the plot of the McCabe-Thiele diagram.
    '''
    
    if not isinstance(xD, (int, float)) or not isinstance(R, (int, float)) or not isinstance(z, (int, float)) or not isinstance(q, (int, float)) or not isinstance(alpha, (int, float)):
        raise TypeError('The inputs must be numbers')

    if xD >= 1 or z >= 1:
        raise ValueError('The fraction must be less than 1')
    if xD <= 0 or z <= 0:
        raise ValueError('xD must be greater than 0')
    if R <= 0:
        raise ValueError('R must be greater than 0')
    if xD <= z:
        raise ValueError('xD must be greater than z')
    
    if F is not None:
        if not isinstance(F, (int, float)):
            raise TypeError('The inputs must be numbers')
        if F <= 0:
            raise ValueError('F must be greater than 0')

    if D is not None:
        if not isinstance(D, (int, float)):
            raise TypeError('D must be a number')
        if D >= F:
            raise ValueError('D must be less than F')

    if xB is not None:
        if not isinstance(xB, (int, float)):
            raise TypeError('xB must be a number')
        if xB >= xD or xB >= z and xB is not None:
            raise ValueError('xB must be greater than z and xD')
        

    

    if xB is None:
        B = F-D
        xB = (z*F-xD*D)/B
    
    x = np.linspace(0,1,1000)

    fig, ax = plt.subplots()

    ahline(ax, xD, 0, xD)
    avline(ax, xD, 0, xD)

    ahline(ax, xB, 0, xB)
    avline(ax, xB, 0, xB)

    x_label(ax, xB, '$x_B$')
    y_label(ax, xB, '$y_B$')

    x_label(ax, xD, '$x_D$')

    x_inter = fsolve(lambda x: enriching_operating_line(R, x, xD) - feed_line(q, z, x), xB)[0]
    x_inter_eq = fsolve(lambda x: equilibrium_line(alpha, x) - enriching_operating_line(R, x, xD), 0)[0]

    
    x_old = x_new = xD
    i = 1
    while x_old > xB:
        ahline(ax, x_old, 0, x_new)
        x_new = fsolve(lambda x: equilibrium_line(alpha, x)-x_old, x_old)[0]

        avline(ax, x_new, 0, equilibrium_line(alpha, x_new))
        x_lab = '$x_{'+str(i)+'}$'
        x_label(ax, x_new, x_lab)

        y_lab = '$y_{'+str(i)+'}$'
        y_label(ax, equilibrium_line(alpha, x_new), y_lab)

        ahline(ax, equilibrium_line(alpha, x_new), 0, x_new)

        if x_new > x_inter:
            x_old = enriching_operating_line(R, x_new, xD)
        else:
            x_old = stripping_operating_line(R, xB, xD, x_inter, x_new)
        
        i += 1
        
        if i > 500:
            raise ValueError('Number of stages exceeds 500. Check the input parameters')

    ax.plot(x, x, "k--", linewidth=0.5)
    ax.plot(x, equilibrium_line(alpha, x), label='equilibrium')
    ax.plot(x[(x>x_inter) & (x<xD)], enriching_operating_line(R, x[(x>x_inter) & (x<xD)], xD), label='enriching operation line')
    ax.plot(x[(x>xB) & (x<x_inter)], stripping_operating_line(R, xB, xD, x_inter, x[(x>xB) & (x<x_inter)]), label='stripping operation line')
    
    


    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    plt.minorticks_on()

    return i-1, fig
