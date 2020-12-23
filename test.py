import numpy as np
import math
import random
from shapely.geometry import LineString
import copy

import timeit

domainI = [1,2,3,4]
dIlenght = len(domainI)
z = 0
while z < dIlenght:
    x = domainI[z]
    if x == 2 or x == 4:
        domainI.remove(x)
        revised = True
        z-=1 
        dIlenght -= 1
    z +=1
print(domainI)
domainI.pop(0)
print(domainI)



