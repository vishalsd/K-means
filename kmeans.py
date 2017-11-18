__author__ = 'Vishal Desai'

import numpy as np
import matplotlib.pyplot as plt
x=np.array([11,18,21,25,6,28,30,32,35,37,38,15,27,36,28,41,25,21,36])
y=np.array([7,8,1,5,6,19,23,27,14,28,31,20,24,31,29,35,36,9,14])

k1x=[]
k1y=[]
k2x=[]
k2y=[]

k1x.append(11)
k1y.append(7)
k2x.append(6)
k2y.append(19)

cluster1x=[]
cluster1y=[]
cluster2x=[]
cluster2y=[]

for i in range(x.size):
    dist1= (((k1x[0]-x[i])**2)+((k1y[0]-y[i])**2)) **(0.5)
    dist2= (((k2x[0]-x[i])**2)+((k2y[0]-y[i])**2)) **(0.5)

    if dist1<dist2:
        cluster1x.append(x[i])
        cluster1y.append(y[i])
    else :
        cluster2x.append(x[i])
        cluster2y.append(y[i])

print cluster1x,cluster1y
print cluster2x,cluster2y
plt.scatter(cluster1x,cluster1y,c="green")
plt.scatter(k1x[0],k1y[0],c="blue")
plt.scatter(cluster2x,cluster2y,c="red")
plt.scatter(k2x[0],k2y[0],c="blue")
plt.show()

k1x.append((int)(np.mean(cluster1x)))
k1y.append((int)(np.mean(cluster1y)))
k2x.append((int)(np.mean(cluster2x)))
k2y.append((int)(np.mean(cluster2y)))

del cluster1x[:]
del cluster1y[:]
del cluster2x[:]
del cluster2y[:]

j=1
while (k1x[j] != k1x[j-1]) or (k2x[j] != k2x[j-1]):
    for i in range(x.size):
        dist1= (((k1x[j]-x[i])**2)+((k1y[j]-y[i])**2)) **(0.5)
        dist2= (((k2x[j]-x[i])**2)+((k2y[j]-y[i])**2)) **(0.5)

        if dist1<dist2:
            cluster1x.append(x[i])
            cluster1y.append(y[i])
        else :
            cluster2x.append(x[i])
            cluster2y.append(y[i])
        print dist1,dist2
    plt.scatter(cluster1x,cluster1y,c="green")
    plt.scatter(k1x[j], k1y[j],c="blue")
    plt.scatter(cluster2x,cluster2y,c="red")
    plt.scatter(k2x[j], k2y[j],c="blue")
    plt.show()
    k1x.append((int)(np.mean(cluster1x)))
    k1y.append((int)(np.mean(cluster1y)))
    k2x.append((int)(np.mean(cluster2x)))
    k2y.append((int)(np.mean(cluster2y)))

    print k1x,k1y,k2x,k2y
    del cluster1x[:]
    del cluster1y[:]
    del cluster2x[:]
    del cluster2y[:]

    j=j+1