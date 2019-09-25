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