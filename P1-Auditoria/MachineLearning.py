# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:56:34 2019

@author: david
"""
#%%
from __future__ import print_function
import pandas as pd
import scipy.stats 
import matplotlib.pyplot as plt
import math as m
pd.__version__

mushroom_dataframe = pd.read_csv("o-database", sep=",")
mushroom_dataframe.describe()

#%%
fig, ax = plt.subplots(5,5)
i = 0
for att in mushroom_dataframe.columns.values:
    mushroom_dataframe[att].value_counts().plot(kind = 'bar', ax=ax[i//5][i%5]).set_title(att)
    i = i+1
fig.set_size_inches(18.5, 18.5, forward=True)
fig.show()

#%%
for att in mushroom_dataframe.columns:
    if(att != 'class'):        
        tab = pd.crosstab(index = mushroom_dataframe['class'], columns = mushroom_dataframe[att], margins=True)
        rows = tab.shape[0]
        columns = tab.shape[1]
        sum = 0
        for i in range(0,rows-2):
            for j in range(0,columns-2):
                p1 = tab.iloc[i][j] / tab.iloc[rows-1][columns-1]
                p2 = tab.iloc[i][j] / tab.iloc[i][columns-1]
                p3 = tab.iloc[i][j] / tab.iloc[rows-1][j]
                x = p1 * m.log10(p1/(p2*p3))
                if(m.isnan(x)):
                    x = 0
                sum += x
        print(str(att), ": ", sum)


#%%
print("Entropy values per category:\n")
for att in mushroom_dataframe.columns:
    p_data = mushroom_dataframe[att].value_counts()           # counts occurrence of each value
    entropy = scipy.stats.entropy(p_data)
    print(str(att),": ",entropy)
  
#%%
mushroom_dataframe = mushroom_dataframe.drop(columns=['veil-type'])
mushroom_dataframe.describe()

#%%
pd.crosstab(index = mushroom_dataframe['stalk-surface-above-ring'], columns = mushroom_dataframe['stalk-surface-below-ring']).plot(kind = 'bar')


#%%
for att in mushroom_dataframe.columns:
    for elem in mushroom_dataframe[att].unique():
        mushroom_dataframe[att + str(elem)] = mushroom_dataframe[att] == elem
mushroom_dataframe.describe()