import numpy as np
import time

""" 
stage = np.matrix('0 0 0 0 0 0 1; 0 0 0 0 0 0 1; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 0 0 0 0; 0 0 0 1 1 1 1 ')
"""

""" 
m = np.arange(49).reshape(7,7)
a = m[2:6,2:4]
b = np.matrix('0 1; 0 1; 1 1; 1 0')

m[2:6,2:4]+=b
 """

def test(l):
    if(len(l)):
        print(l.pop())
        time.sleep(1)
        return test(l)
    else:
        print(0)
        return 0

a = [1,2,3,4,5,6,7,8,9,10]
test(a)
