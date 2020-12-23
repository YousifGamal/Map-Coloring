import numpy as np
import math
import random
from shapely.geometry import LineString
import copy

import timeit

colors = ['r','g','b','y']
domain = []
start = timeit.default_timer()
for i in range(50):
    domain.append(copy.deepcopy(colors))

stop = timeit.default_timer()

print('Time: ', stop - start)
start = timeit.default_timer()
orig = copy.deepcopy(domain)


stop = timeit.default_timer()

print('Time: ', stop - start)




