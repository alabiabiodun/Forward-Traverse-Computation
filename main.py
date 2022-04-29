# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:09:18 2018

@author: Alabi Abiodun
"""

import pandas as pd
import math
import dms2degrees
import numpy as np
import degrees2dms
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

root.file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("Excel files","*.xls"),("all files","*.*")))


dms = degrees2dms.deg2dms

#from functools import partial

deg = dms2degrees.dms2deg
#df = pd.read_excel('C:\\Users\\Alabi\\Desktop\\data999.xls',header = None, names = ['Distance','deg','mins','secs','Easting','Northing','ID'], na_values = ['',''])
#df.fillna(0)
#r,c = df.shape

'''df.iloc[1,4] = df.iloc[0,4] + df.iloc[1,0] * math.sin(math.radians(deg([df.iloc[1,1],df.iloc[1,2],df.iloc[1,3]])))

for i in range(2,r):
            
    if i < r:
        df.iloc[i,4] = df.iloc[i-1,4] + df.iloc[i,0] * math.sin(math.radians(deg([df.iloc[i,1],df.iloc[i,2],df.iloc[i,3]])))
                
    else:
        break
            
print(df.iloc[:,4])'''


'''for i in range(r):
            
    if i < r-1:
        df.iloc[i+1,4] = df.iloc[i,4] + df.iloc[i+1,0] * math.sin(math.radians(deg([df.iloc[i+1,1],df.iloc[i+1,2],df.iloc[i+1,3]])))
                
    else:
        break
            
print(df.iloc[:,4])'''
        
class coordinatesComputation:
    df = pd.read_excel(root.file_path,header = None, names = ['Distance','deg','mins','secs','Easting','Northing','ID'], na_values = ['',''], index = False)
    df.fillna(0)
    r,c = df.shape
    
    print('Distance(m)','\t','Bearing','\t',df.columns[4] +'(mE)','\t',df.columns[5]+'(mN)','\t',df.columns[6])  
    print('','\t\t','','\t\t','{}'.format('%0.3f'%df.iloc[0,4]),'\t','{}'.format('%0.3f'%df.iloc[0,5]),'\t',df.iloc[0,6])
    #data = np.matrix(df)

    #r,c = data.shape
    df.iloc[1,4] = df.iloc[0,4] + df.iloc[1,0] * math.sin(math.radians(deg([df.iloc[1,1],df.iloc[1,2],df.iloc[1,3]])))
    df.iloc[1,5] = df.iloc[0,5] + df.iloc[1,0] * math.cos(math.radians(deg([df.iloc[1,1],df.iloc[1,2],df.iloc[1,3]])))    
    
    for i in range(2,r):
      
      if i < r:
           df.iloc[i,4] = df.iloc[i-1,4] + df.iloc[i,0] * math.sin(math.radians(deg([df.iloc[i,1],df.iloc[i,2],df.iloc[i,3]])))
           df.iloc[i,5] = df.iloc[i-1,5] + df.iloc[i,0] * math.sin(math.radians(deg([df.iloc[i,1],df.iloc[i,2],df.iloc[i,3]])))     
      else:
           
           break
            
             
    
    def Coordinates(self):
        for i in range(self.r-2):
            if len(str(int(self.df.iloc[i+1,0]))) == 1 :
              
                print('0%0.3f'%self.df.iloc[i+1,0],'\t\t','{}'.format(dms(deg([self.df.iloc[i+1,1],self.df.iloc[i+1,2],self.df.iloc[i+1,3]]))),'\t','%0.3f'%self.df.iloc[i+1,4],'\t','%0.3f'%self.df.iloc[i+1,5],'\t',self.df.iloc[i+1,6])
            
            else:
                print('%0.3f'%self.df.iloc[i+1,0],'\t\t','{}'.format(dms(deg([self.df.iloc[i+1,1],self.df.iloc[i+1,2],self.df.iloc[i+1,3]]))),'\t','%0.3f'%self.df.iloc[i+1,4],'\t','%0.3f'%self.df.iloc[i+1,5],'\t',self.df.iloc[i+1,6])
            
      
        
compute = coordinatesComputation()
compute.Coordinates()
    
