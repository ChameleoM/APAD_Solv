import pickle
import numpy as np

#返回第一个item在matr中的位置，编号从0开始
def findItem(matr,item):
    ind = -99
    w = matr.shape[1]
    for i in range(matr.A1.size):
        if matr.A1[i] == item:
            ind = i
            break
    if ind==-99:
        return 'not found'
    else:
        row = int((ind)/w)
        col = (ind)%w
        return [row,col]

#判断是否放得下拼图
def pcSetable(matr,pc):
    leftup = findItem(matr,0)
    ma = matr.shape[0]
    mb = matr.shape[1]
    pa = pc.shape[0]
    pb = pc.shape[1]
    la = leftup[0]
    lb = leftup[1]
    if(pa+la<=ma and pb+lb<=mb):
        return True
    else:
        return False


stage = np.matrix('0 0 0 0 0 0 1; 0 0 0 0 0 0 1; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 1 1 1 1 ')
pcStyleList = []
indexList = list(range(8))


""" 
with open('pcs.pk', 'r+b') as f:
    pcStyleList = pickle.load(f)
f.close()
 """
