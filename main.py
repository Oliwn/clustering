# Gralf Antiga, Oliver Strauss
# repository link: https://github.com/Oliwn/clustering
# clustering

from scipy.spatial.distance import cityblock
import pandas as pd
import random

#Gets the minimum element of a list (needed because the built-in function didn't work with floats)
def getMin(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

#Returns new coordinates for a specified cluster
def getCentroidCoordinates(cendist, data):
    sumx = 0
    sumy = 0
    for dist in cendist:
        sumx += data.iloc[dist[1]][0]
        sumy += data.iloc[dist[1]][1]

    sumx /= len(cendist)
    sumy /= len(cendist)

    return [sumx, sumy]

#Checks if all the coordinates in the two list are the same
def centroidsChanged(centroids, newCentroids):
    for x in range(len(centroids)):
        if (centroids[x][0] != newCentroids[x][0] or centroids[x][1] != newCentroids[x][1]):
            return True
    return False

#Reads the whole csv File
csvFile = pd.read_csv('input.csv', decimal=",", sep=";", header=None, dtype=float)

numofcluster=int(csvFile.iloc[0,0])


#Reads the csv File, but skips the first 2 rows
data=pd.read_csv('input.csv', decimal=",", sep=";", skiprows=2, header=None, dtype=float) #same function as inline 9 without the first 2 rows

#looks for min/max of the input file in order to get the boundaries for the random kpoints
minval=data.min()
maxval=data.max()


#generating random k points and adding it to an array
centroids = []
for x in range(numofcluster):
    a=random.uniform(minval[0],maxval[0])
    b=random.uniform(minval[1],maxval[1])
    centroids.append([a,b])


cendists=[]
changed = True
count = 0

while (changed):
    #creates a list of lists with all calculated distances between each point and each kpoint
    cendists=[]
    for i in range(numofcluster):
        cendists.append([])

    #calculates distances between each point and each kpoint
    for x in range(len(data)):
        distances=[]
        for centroid in centroids:
            distances.append(cityblock(centroid, data.iloc[x]))

        #saves the smallest distance of a point to its corresponding kpoint
        min = getMin(distances)
        cendists[distances.index(min)].append([min, x])

    #calculates the new location for each kpoint
    newCentroids=[]
    for i in range(len(cendists)):
        newCentroids.append(getCentroidCoordinates(cendists[i], data))

    #sets the new locations of the kpoint and checks they changed, if not the loop is broken
    if centroidsChanged(centroids, newCentroids):
        changed = True
        centroids = newCentroids
    else:
        changed = False

    print("centroids new")
    print(centroids)
    count += 1

print(count)

#writes the result into a csv File
file = open("output.csv", "w")
file.write(str(numofcluster) + "\n")

for centroid in centroids:
    file.write(str(centroid[0]) + ";" + str(centroid[1]) + "\n")

file.write(str(count) + "\n")
file.write(str(csvFile.iloc[1,0]) + ";" + str(csvFile.iloc[1,1]) + "\n")

for i in range(len(cendists)):
    for x in cendists[i]:
        file.write(str(i) + ";" + str(data.iloc[x[1],0]) + ";" + str(data.iloc[x[1],1]) + "\n")
