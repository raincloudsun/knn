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

def kSet(kCount,s):
    res = []
    for i in range(dataSize):
        tmp = []
        for j in range(kCount):
            tmp.append(s[j][i])
        m = min(tmp)
        res.append(tmp.index(m))

    return res


def kSetCentroid(kCount,kx,ky,x,y,k):
    colorSeed = 30
    cmap = plt.cm.get_cmap("nipy_spectral", 256)

    sumx = [0] * len(k)
    sumy = [0] * len(k)
    count= [0] * len(k)
    retryFlag= [0] * kCount

    for i in range(len(k)):
        plt.scatter(x[i], y[i], label="circle", color=cmap(k[i]*colorSeed), marker= ".", s=30) 

        # kset sum
        sumx[k[i]] += x[i]
        sumy[k[i]] += y[i]
        count[k[i]]+= 1

    for i in range(kCount):
        ax.scatter(kx[i], ky[i], label="stars", color=cmap(i*colorSeed), marker="^", s=100)

        # centroid campare
        avgx = sumx[i] / count[i]
        avgy = sumy[i] / count[i]
        if kx[i]==avgx and ky[i]==avgy:
            retryFlag[i] = 1

        # next centroid
        kx[i] = avgx
        ky[i] = avgy

    return retryFlag


def kmeans(kCount,x,y):
    kx = random.sample(range(dataSize), kCount)
    ky = random.sample(range(dataSize), kCount)

    for i in range(updLimits):
        sv = Euclidean(kCount,kx,ky,x,y)
        kr = kSet(kCount,sv)
        ret= kSetCentroid(kCount,kx,ky,x,y,kr)

        trueCount = 0
        for j in range(kCount):
            if ret[j] == 1: 
                trueCount += 1

        plt.pause(0.1)

        if trueCount == kCount:
            print "kset centroid complete !"
            break
        else:
            print "retry kset-centroid...%d" % trueCount
            ax.clear()

        #reset centroid point
        #plt.draw() 

    plt.waitforbuttonpress()


x = []
y = []
xTable = {}
yTable = {}

def setItem(i,index,table,data):
    if table.get(data) == None:
        table[data] = index
        index += 1

    i.append(table[data])
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
        xIndex = setItem(x, xIndex, xTable, r[0])
        yIndex = setItem(y, yIndex, yTable, r[1])

    f.close()

    #print x
    #print y

    plt.scatter(x, y, label="circle", color='black', marker= ".", s=30) 
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

    vectorize(x, y)
    

# End of File
