# Clustering
#oli stinkt

from scipy.spatial.distance import cityblock
import pandas as pd
import random

def getMin(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def getCentroidCoordinates(cendist, data):
    sumx = 0
    sumy = 0
    for dist in cendist:
        sumx += data.iloc[dist[1]][0]
        sumy += data.iloc[dist[1]][1]

    sumx /= len(cendist)
    sumy /= len(cendist)

    return [sumx, sumy]

def centroidsChanged(centroids, newCentroids):
    for x in range(len(centroids)):
        if (centroids[x][0] != newCentroids[x][0] or centroids[x][1] != newCentroids[x][1]):
            return True
    return False

data = pd.read_csv('input.csv', sep=";", header=None, dtype=float)

numofcluster=int(data.iloc[0,0])



#looks for min/max of the input file in order to get the boundaries for the random kpoints
df=pd.read_csv('input.csv', sep=";", skiprows=2, header=None, dtype=float) #same function as inline 9 without the first 2 rows

minval=df.min()
maxval=df.max()


#generating random k points and adding it to an array
centroids = []
for x in range(numofcluster):
    a=random.uniform(minval[0],maxval[0])
    b=random.uniform(minval[1],maxval[1])
    centroids.append([a,b])

#creates a list with all calculated distances between each point and each kpoint
cendist1=[]
cendist2=[]
cendist3=[]

changed = True

while (changed):
    for x in range(len(df)):
        distances=[]
        distances.append(cityblock(centroids[0], df.iloc[x]))
        distances.append(cityblock(centroids[1], df.iloc[x]))
        distances.append(cityblock(centroids[2], df.iloc[x]))

        #print()
        #print(distances)

        min = getMin(distances)
        if (distances.index(min) == 0):
            cendist1.append([min, x])
        elif (distances.index(min) == 1):
            cendist2.append([min, x])
        else:
            cendist3.append([min, x])

    print("centroids old")
    print(centroids)
    newCentroids = []
    newCentroids.append(getCentroidCoordinates(cendist1, df))
    newCentroids.append(getCentroidCoordinates(cendist2, df))
    newCentroids.append(getCentroidCoordinates(cendist3, df))

    if (centroidsChanged(centroids, newCentroids)):
        changed = True
        centroids = newCentroids
    else:
        changed = False

    print("centroids new")
    print(centroids)

#for points in range(len(df)):

 #   dist1=cityblock(centroids[0],df.iloc[points])
  #  dist2=cityblock(centroids[1],df.iloc[points])
   # dist3= cityblock(centroids[2],df.iloc[points])

#    cendist1.append(dist1)
 #   cendist2.append(dist2)
  #  cendist3.append(dist3)
#print()
#print(cendist1)
#print(cendist2)
#print(cendist3)
#print()
#print(len(cendist1))
#print(len(cendist2))
#print(len(cendist3))

#checks which kpoint is closer to each data entry and saves the data in the kpoint list to which its closer to
#here is an error in line 63, schau dir einfach die fehlermeldung an die ergibt kein sinn,
#deshalb hab ich auch soviele prints um zu checken was los ist
#tldr: sie sagen dass der index temp out of range ist bei ca wert 10 obwohl die liste bis 18 geht also auch der index
#for temp in range(len(cendist1)):
#    print(temp)
#    if cendist1[temp] < cendist2[temp] and cendist1[temp] < cendist3[temp]:
#        cendist2.pop(temp)
#        cendist3.pop(temp)
#    elif cendist2[temp] < cendist1[temp] and cendist2[temp] < cendist3[temp]:
#        cendist1.pop(temp)
#        cendist3.pop(temp)
#    elif cendist3[temp] < cendist2[temp] and cendist3[temp] < cendist1[temp]:
#        cendist2.pop(temp)
#        cendist1.pop(temp)

#print("new list")
#print(cendist1)
#print(cendist2)
#print(cendist3)
#next step: calculate the average of each list and define them as new k-points
#loop the whole thing
#creat export file with the numbers
#for the export file: important to implement a counter that counts how often a dataset got a signed to a cluster
#for better reference check output.csv