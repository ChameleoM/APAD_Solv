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
        return 0
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

#设置日期
def setDate(date):
    stage =stageInit()
    mon = date[0]
    day = date[1]
    dr = (day+13)//7
    dc = (day+13)%7
    if(mon<=6):
        stage[0,mon-1] = 1
    else:
        stage[1,mon-7] = 1
    stage[dr,dc] = 1
    return stage

#重置网格
def stageInit():
    return(np.matrix('0 0 0 0 0 0 1; 0 0 0 0 0 0 1; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 1 1 1 1 '))

def main(date):
    dateToSolv = setDate(date)

    while(findItem(dateToSolv,0)):
        pass

pcStyleList = []
indexList = list(range(8))
date = [12,3]






""" 
with open('pcs.pk', 'r+b') as f:
    pcStyleList = pickle.load(f)
f.close() 
 """
