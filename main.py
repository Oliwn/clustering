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
#creates a list with all calculated distances between each point and each kpoint
cendist1=[]
cendist2=[]
cendist3=[]

for points in range(len(df)):

    dist1=cityblock(centroids[0],df.iloc[points])
    dist2=cityblock(centroids[1],df.iloc[points])
    dist3= cityblock(centroids[2],df.iloc[points])

    cendist1.append(dist1)
    cendist2.append(dist2)
    cendist3.append(dist3)
print()
print(cendist1)
print(cendist2)
print(cendist3)
print()
print(len(cendist1))
print(len(cendist2))
print(len(cendist3))

#checks which kpoint is closer to each data entry and saves the data in the kpoint list to which its closer to
for temp in range(len(cendist1)):
    print(temp)
    if cendist1[temp] < cendist2[temp] and cendist1[temp] < cendist3[temp]:
        cendist2.pop(temp)
        cendist3.pop(temp)
    elif cendist2[temp] < cendist1[temp] and cendist2[temp] < cendist3[temp]:
        cendist1.pop(temp)
        cendist3.pop(temp)
    elif cendist3[temp] < cendist2[temp] and cendist3[temp] < cendist1[temp]:
        cendist2.pop(temp)
        cendist1.pop(temp)

print("new list")
print(cendist1)
print(cendist2)
print(cendist3)
#next step: calculate the average of each list and define them as new k-points
#loop the whole thing
#creat export file with the numbers
#for the export file: important to implement a counter that counts how often a dataset got a signed to a cluster
#for better reference check output.csv