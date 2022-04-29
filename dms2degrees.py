# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:24:38 2018

@author: Alabi
"""

def dms2deg(dms = []):
    d = dms[0]
    m = dms[1]
    s = dms[2]
    
    #dd = d + (m + s/60)/60
    
    
    if d < 0:
        dd = -1 * (abs(d) + (m + s/60)/60)
        
    else:
        dd = d + (m + s/60)/60
        
    return dd       
        