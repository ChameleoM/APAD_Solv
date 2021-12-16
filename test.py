import numpy as np
import pickle

#4个方向
def fourWay(pc):
    s =[pc]
    for i in range(3):
        pc=np.rot90(pc)
        s.append(pc)
    return s

#去重
def uniquePcList(pcList):
    b = set()
    c = []
    for x in pcList:
        key = repr(x)
        if key not in b:
            b.add(key)
            c.append(x)
    return c

#一片拼图的所有姿势
def pcStyles(pc):
    a = fourWay(pc)
    b = fourWay(pc.T)
    c = uniquePcList(a+b)
    return c


pcU = np.matrix('1 0 1; 1 1 1')
pcL = np.matrix('1 1 1; 1 0 0; 1 0 0')
pcLL = np.matrix('0 0 0 1; 1 1 1 1')
pcIdx = np.matrix('1 1; 1 1; 1 0')
pcSqr = np.matrix('1 1 1; 1 1 1')
pcGun = np.matrix('1 1 1 1; 0 0 1 0')
pcZ = np.matrix('1 1 0; 0 1 0; 0 1 1')
pcLz = np.matrix('0 0 1 1; 1 1 1 0')

pcList = [pcU,pcL,pcLL,pcIdx,pcSqr,pcGun,pcZ,pcLz]

pcShapeLib = []

for pc in pcList:
    pcShapeLib.append(pcStyles(pc))

with open('pcs.pk', 'w+b') as f:
    pickle.dump(pcShapeLib, f)
f.close()