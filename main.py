# Clustering
#oli stinkt

from scipy.spatial.distance import cityblock
import pandas as pd
import random


data = pd.read_csv('input.csv', sep=";", header=None, dtype=float)
print (data)
numofcluster=int(data.iloc[0,0])

print(cityblock(data.iloc[2], data.iloc[3]))
print(numofcluster)
print()

#looks for min/max of the input file in order to get the boundaries for the random kpoints
df=pd.read_csv('input.csv', sep=";", skiprows=2, header=None, dtype=float) #same function as inline 9 without the first 2 rows
print(df)
minval=df.min()
maxval=df.max()
print(minval)
print(maxval)

#generating random k points and adding it to an array
centroids = []
for x in range(numofcluster):
    a=random.uniform(minval[0],maxval[0])
    b=random.uniform(minval[1],maxval[1])
    centroids.append([a,b])

print(centroids)
print(centroids[0])
print(centroids[1])
print(centroids[2])