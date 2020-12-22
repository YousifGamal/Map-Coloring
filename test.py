import numpy as np
import math
import random
from shapely.geometry import LineString
import copy

queue = []
for i in range(4):
    newArc = (i,i)
    queue.append(newArc)

print(queue)
