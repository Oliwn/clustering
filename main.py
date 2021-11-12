# Clustering
#oli stinkt

from scipy.spatial.distance import cityblock
import pandas as pd

data = pd.read_csv('input.csv', sep=";", header=None, dtype=float)
print (data)
numofcluster=data.iloc[0,0]
print(cityblock(data.iloc[2], data.iloc[3]))
print(numofcluster)
