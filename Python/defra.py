from cycler import cycler
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import itertools
#print(mpl.rcParams.keys())



def defra_plots(form='A4'):
    form_options = ['A4','slide-pack','A0']
    if form not in form_options:
        raise ValueError(form+' invalid: use one of the following: '+str(form_options))
        
    width_dict ={'A4':6.948819, 'slide-pack':6.133858, 'A0':(3*33.125/20.0)}
    height_dict ={'A4':3.357143, 'slide-pack':3.614173, 'A0':(46.8125/3.5)}
    width_ = width_dict[form]
    height_ = height_dict[form]
    
    mpl.rcParams['axes.prop_cycle'] = (cycler(color=['#006837', '#31a354', '#78c679', '#c2e699'])+
                                       cycler(linestyle=['-', '--', ':', '-.']))
    mpl.rcParams['figure.figsize'] = (width_, height_)
    mpl.rcParams['lines.linewidth'] = 2.5
    mpl.rcParams['lines.markersize'] = 5
    mpl.rcParams['scatter.marker'] =  'x'
    mpl.rcParams['savefig.bbox'] = 'tight'
    mpl.rcParams.update({"axes.grid" : True, "grid.color": "lightgrey", 'grid.linestyle':(0,(5,10))})
