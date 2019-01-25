import matplotlib.pyplot as plt 
import random
import numpy as np

plt.ion()
flg, ax = plt.subplots()

dataSize    = 1000
updLimits   = 100

def Euclidean(kCount,kx,ky,x,y):
    ss = []
    for i in range(kCount):
        s = []
        for j in range(dataSize):
            v = (kx[i]-x[j])**2 + (ky[i]-y[j])**2
            s.append(v)
        ss.append(s)
    return ss

seed = ['orange','green','blue','purple','midnightblue','forestgreen','goldenrod','c','naby','deepskyblue','olivedrab','sienna','maroon','dimgrey','m']

x = []
y = []
xTable = {}
yTable = {}

user = '535220'
xUser = []
yUser = []

def setItem(i,index,table,data):
    if table.get(data) == None:
        table[data] = index

    i.append(table[data])
    index += 1
    return index

def vectorize(x, y):
    xIndex = 0
    yIndex = 0

    f = open("qr.csv", 'r')
    while True:
        line = f.readline()
        if not line: break

        r = line.split(',')
        r[1] = r[1].split('\r\n')[0]
        #print r
        if r[0] == user:
            xIndex = setItem(xUser, xIndex, xTable, r[0])
            yIndex = setItem(yUser, yIndex, yTable, r[1])
        else:
            xIndex = setItem(x, xIndex, xTable, r[0])
            yIndex = setItem(y, yIndex, yTable, r[1])

    f.close()

    print xUser
    print yUser

    plt.scatter(x, y, color='grey', marker= ".", s=20) 
    #plt.scatter(xUser, yUser, color='red', marker= ".", s=30) 

    for i in range(len(y)):
        for j in range(len(yUser)):
            if y[i] == yUser[j]:
                for k in range(len(x)):
                    if x[i] == x[k]:
                        plt.scatter(x[k], y[k], color=seed[j], marker= "^", s=35, vmin=10) 

                #print x[i], y[i]

    plt.waitforbuttonpress()

def vectorize2(x, y):
    xIndex = 0
    yIndex = 0

    f = open("qr.csv", 'r')
    while True:
        line = f.readline()
        if not line: break

        r = line.split(',')
        r[1] = r[1].split('\r\n')[0]

        if int(r[0]) > 2:
            xUser.append(r[1])
            yUser.append(r[0])
        else:
            print r

    f.close()

    plt.scatter(xUser, yUser, color='black', marker= ".", s=10) 
    plt.waitforbuttonpress()

if __name__ == "__main__":

    '''
    # cluster count
    k =10 

    # x, y coordinates
    x = random.sample(range(dataSize), dataSize)
    y = random.sample(range(dataSize), dataSize)

    # run k-means
    kmeans(k, x, y)
    '''

    #vectorize(x, y)
    vectorize2(x, y)
    

# End of File
