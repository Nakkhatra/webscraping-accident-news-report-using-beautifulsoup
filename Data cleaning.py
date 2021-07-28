# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 05:12:32 2021

@author: snakk
"""

import pandas as pd 
import re
import os
import numpy as np

df= pd.read_csv(r"E:\Machine Learning\Webscraping\RoadAccidentsTheDailyObserver-final.csv")



#df["bool"]= [(df["titles"][i] in df["News"][i]) for i in range(df.shape[0])]
#df["replaced"]=[(df["News"][i].replace(df["titles"][i],"")) for i in range(df.shape[0])]

# =============================================================================
# #Removing the headline/title from the newsbody first, because of the improper punctuation and lack of whitespace
# 
# def getit(row):
#  try:
#   return row.News.replace(row.titles,"")
#  except:
#   return row.News # in case row.get("titles") return non-string
# 
# df["replaced"] = df.apply(getit , axis = 1)
# 
# df= df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
# 
# 
# #Adding the headline to the news body with a colon................
# df["cleaned"]= df.titles+": "+df.replaced
# =============================================================================

#First, let's strip off the beginning and ending whitespaces from the whole
#dataframe if the entries are string===========================================

df= df.applymap(lambda x: x.strip() if isinstance(x, str) else x)   #.apply() is for a single pd series while .applymap() applies for the whole dataframe

#Now, let's use apply method to replace the headlines that are already on the Newsbody
#with proper punctuation ": " and those news which do not have title in the body, add
#the title to the body for those with a ": "

def addheadlines(row):
    if row.titles in row.News:
        try:
            return row.News.replace(row.titles,row.titles+": ")
        except:
            return row.News # in case row.get("titles") return non-string
        
    else:
        return row.titles+": "+row.News

df["combined"]= df.apply(addheadlines, axis="columns")

#Extracting the time of accident from the combined news body using regex=======
time_of_accident=[]

for news in df.combined:
    match= re.search(r'\d*\W*\d+\s*([pP]|[aA])[mM]',news)
    if match!=None:
        time_of_accident.append(match.group(0).strip())
    else:
        time_of_accident.append(None)
        
df["time_of_accident"]=time_of_accident

#Swapping columns to arrange===================================================
columns_titles = ["links","titles","News","combined","Year","day","date","time_of_accident","time","time_desc"]
df=df.reindex(columns=columns_titles)

#Renaming time column to publish time==========================================
columns_titles = ["links","titles","News","combined","Year","day","date","time_of_accident","publish_time","time_desc"]
df.columns= columns_titles

#Creating a new bool series for identifying news reports with multiple accidents
df["multiple"]=np.zeros(df.shape[0])

index=0

for news in df.combined:
    if "accidents" in news:
        df.multiple[index]= 1
    index+=1
    
#Removing train accidents only and Peru accidents==============================
rows=[]
index=0
for news in df.combined:
    if "train accident" in news or "Peru" in news:
        rows.append(index)
    index+=1
#Dropping the train accidents and Peru accident from df========================
df= df.drop(rows, axis=0)
#Resetting index after dropping those rows=====================================
df= df.reset_index(drop=True)

#repeating the multiple news reports for 5 times each==========================
df = pd.DataFrame(np.repeat(df.values, df['multiple']*4+1, axis=0), columns=df.columns)
    
path=r"E:\Machine Learning\Webscraping"
df.to_csv(os.path.join(path,'RoadAccidentsTheDailyObserver-cleaned-final.csv'),index=False, encoding= 'utf-8-sig')