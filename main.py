# Clustering
#oli stinkt

from scipy.spatial.distance import cityblock
import pandas as pd

data = pd.read_csv('input.csv', sep=";", header=None, skiprows=2, dtype=float)
print (data)

print(cityblock(data.iloc[0], data.iloc[1]))