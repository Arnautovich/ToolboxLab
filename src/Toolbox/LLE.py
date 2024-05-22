import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from typing import Union
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


def ahline(ax:object, y:float, xmin:float, xmax:float) -> None:
    '''
    This function draws a horizontal line on the plot. The input parameters are:
    ax: the axis object
    y: the y-coordinate of the horizontal line
    xmin: the starting x-coordinate of the line
    xmax: the ending x-coordinate of the line
    '''
    ax.axhline(y=y,xmin=xmin, xmax=xmax, linestyle='--', color='black', dash_capstyle='round', linewidth=0.9)

def avline(ax:object, x:float, ymin:float, ymax:float) -> None:
    '''
    This function draws a vertical line on the plot. The input parameters are:
    ax: the axis object
    x: the x-coordinate of the vertical line
    ymin: the starting y-coordinate of the line
    ymax: the ending y-coordinate of the line
    '''
    ax.axvline(x=x,ymin=ymin, ymax=ymax, linestyle='--', color='black', dash_capstyle='round', linewidth=0.9)

def equilibrium_line(kD:float, x:Union[np.ndarray, float]) -> Union[np.ndarray, float]:
    '''
    This function calculates the equilibrium value of x given alpha. The input parameters are:
    alpha: Relative volatility of the light component with respect to the heavy component
    x: a float or an array of floats representing the points at which the equilibrium value of x is to be calculated
    '''
    return kD*x

def x_label(ax:object, x:float, text:str) -> None:
    '''
    This function adds a label to the x-axis. The input parameters are:
    ax: the axis object
    x: the x-coordinate of the label
    text: the text of the label
    '''
    ax.annotate(text, textcoords = 'offset points', xy=(x, 0), xytext=(8,3), ha='center', fontsize=10, color='black',fontname='Arial')

def y_label(ax:object, y:float, text:str) -> None:
    '''
    This function adds a label to the y-axis. The input parameters are:
    ax: the axis object
    y: the y-coordinate of the label
    text: the text of the label
    '''
    ax.annotate(text, textcoords = 'offset points', xy=(0, y), xytext=(8,5), ha='center', fontsize=10, color='black',fontname='Arial')


def operating_line(R:float, x:Union[np.ndarray, float], yN_1:float, E:float, xN:float) -> Union[np.ndarray, float]:
    '''
    This function calculates the enriching operating line. The input parameters are:
    R: feed/raffinate feed
    

    '''
    return R/E* x + (yN_1 - R/E * xN)

def lle(R:Union[float,int], E:Union[float,int], x0:float, xN:float, yN_1:float, kD:float) -> Union[object,float]:
    '''
    This function plots the liquid-liquid equilibrium diagram for counter-current operation. The input parameters are:
    R: feed/Raffinate flow rate
    E: extract/solvent flow rate
    x0: feed composition
    xN: raffinate composition at the end of the column
    yN_1: solvent composition at the start of the column
    kD: relative volatility of the light component with respect to the heavy component

    Output:
    fig: the figure object of the plot
    i: the number of stages required for the separation

    Assumptions with Dilute case:
    1. Constant equilibrium constant (kD)
    2. Constant feed/raffinate flow rate (R)
    3. Constant extract/solvent flow rate (E)
    '''
    
    var = {'R':R, 'E':E, 'x0':x0, 'xN':xN, 'yN_1':yN_1, 'kD':kD}

    for key in var.keys():
        if not isinstance(var[key], (int, float)):
            raise TypeError(f'{key} must be an integer or a float')
    
    if x0 >1 or xN > 1 or yN_1 > 1:
        raise ValueError('Fraction must be less than 1')

    if x0 < xN:
            raise ValueError('x0 must be greater than xN')

    fig, ax = plt.subplots()
    xmax = x0+0.05*x0
    ymax = equilibrium_line(kD, xmax)

    avline(ax, x0, 0, operating_line(R, x0, yN_1, E, xN)/ymax)
    x_label(ax, x0, '$x_0$')
    ahline(ax, operating_line(R, x0, yN_1, E, xN), 0, x0/xmax)
    y_label(ax, operating_line(R, x0, yN_1, E, xN), '$y_1$')

    avline(ax, xN, 0, operating_line(R, xN, yN_1, E, xN)/ymax)
    x_label(ax, xN, '$x_N$')
    
    x = np.linspace(0,1,1000)
    xi = x0
    i = 1
    while xi > xN:
        yi_1 = operating_line(R, xi, yN_1, E, xN)
        xi = fsolve(lambda x: equilibrium_line(kD, x)-yi_1, xi)[0]

        if xi < xN:
            break
        
        avline(ax, xi, 0, equilibrium_line(kD,xi)/ymax)
        x_label(ax, xi, f'$x_{i}$')
        ahline(ax, operating_line(R, xi, yN_1, E, xN), 0, xi/xmax)

        y_label(ax, operating_line(R, xi, yN_1, E, xN), f'$y_{i+1}$')

        i += 1

        if i > 500:
            raise ValueError('Number of stages exceeds 500. Check the input parameters')


    ax.plot(x, equilibrium_line(kD, x), label='equilibrium')
    ax.plot(x, operating_line(R, x, yN_1, E, xN), label='Operation line')
    
    
    ax.set_xlim(0,x0+0.05*x0)
    ax.set_ylim(0,equilibrium_line(kD, xmax))
    
    ax.xaxis.set_major_locator(MultipleLocator((x0+0.05*x0)/5))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))


    return fig, i


def LLE_cross_flow(R:Union[float,int], E:Union[float,int], x0:float, xN:float, y_in:float, kD:float) -> Union[object,float]:
    '''
    This function plots the liquid-liquid equilibrium diagram for cross-flow operation. The input parameters are:
    R: feed/Raffinate flow rate
    E: extract/solvent flow rate
    x0: feed composition
    xN: raffinate composition at the end of the column
    y_in: solvent composition for each stage
    kD: equilibrium constant

    Output:
    fig: the figure object of the plot
    i: the number of stages required for the separation

    Assumptions with Dilute case:
    1. Constant equilibrium constant (kD)
    2. Constant feed/raffinate flow rate (R)

    Other assumption:
    1. The solvent composition is constant for each stage
    '''

    var = {'R':R, 'E':E, 'x0':x0, 'xN':xN, 'y_in':y_in, 'kD':kD}

    for key in var.keys():
        if not isinstance(var[key], (int, float)):
            raise TypeError(f'{key} must be an integer or a float')
        
    if x0 >1 or xN > 1 or y_in > 1:
        raise ValueError('Fraction must be less than 1')
    
    if x0 < xN:
            raise ValueError('x0 must be greater than xN')
    
    
    fig, ax = plt.subplots()
    xmax = x0+0.05*x0
    ymax = equilibrium_line(kD, xmax)

    slope = R/E

    x = np.linspace(0,1,100000)
    

    xj_1 = x0
    i = 1

    
    while xj_1 > xN:
        inter = fsolve(lambda x: -slope*x+(slope*xj_1+y_in)-equilibrium_line(kD, x), xj_1)[0]

        ax.plot(x[(x>inter) & (x<xj_1)], -slope*x[(x>inter) & (x<xj_1)]+(slope*xj_1+y_in), label='operating line', color='blue')

        xj_1 = inter

        avline(ax, inter, 0, equilibrium_line(kD, inter)/ymax)

        i += 1

        if i > 500:
            raise ValueError('Number of stages exceeds 500. Check the input parameters')
        
    ax.plot(x, equilibrium_line(kD, x), label='equilibrium', color='red')

    
    
    ax.set_xlim(0,x0+0.05*x0)
    ax.set_ylim(0,equilibrium_line(kD, xmax))
    
    ax.xaxis.set_major_locator(MultipleLocator((x0+0.05*x0)/5))
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))

    return fig, i-1