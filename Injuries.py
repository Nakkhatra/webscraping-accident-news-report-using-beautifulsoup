# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:50:31 2021

@author: snakk
"""

import pandas as pd
import numpy as np
import os

df= pd.read_csv("E:\Machine Learning\Omdena\Task 2\RoadAccidentsTheDailyObserver-cleaned-final (2).csv")

Injurybool=np.zeros(df.shape[0])
index=0
for news in df.combined:
    if "injur" in news:
        Injurybool[index]=1
    else:
        df["Number_of_injuries"][index]=0
    index+=1

df["Injurybool"]=Injurybool
    
path=r"E:\Machine Learning\Omdena"
#print(df)
df.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver-finalinjury.csv'),index=False, encoding= 'utf-8-sig')

        
        
        