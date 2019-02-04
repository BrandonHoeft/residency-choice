#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 16:32:30 2019
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm #color maps
import joypy
import numpy as np # to make random draws. 
import os

os.chdir('/Users/bhoeft/Desktop/residency-choice')

file = 'Residency Feelings.csv'
df = pd.read_csv(file, parse_dates=['date'])
df.info()

df.describe()
search = df.agg('std') == 0# schools with no variance rankings
ranks_with_no_variance = df.agg('std').index[search].tolist()


# Understand the center, variance of each School's ratings
df2 = df.copy()
df2[ranks_with_no_variance] = (df2[ranks_with_no_variance].apply(lambda x: np.random.normal(x, 0.25, df.shape[0])))


df.agg('median').sort_values()
rank_by_lowest_median = df.agg('median').sort_values().index

joypy.joyplot(df2, overlap=3, 
              labels = rank_by_lowest_median,
              colormap=cm.coolwarm,
              title='Daily Program Rank Distribution: ordered by median rank',
              figsize=(10,8)) #https://github.com/sbebo/joypy/blob/master/Joyplot.ipynb

plt.show()
plt.savefig('Daily Program Rank Distribution.png')