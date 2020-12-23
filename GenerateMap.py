import numpy as np
from shapely.geometry import LineString
import math 
import random
import timeit

def GenerateNPoints(n):
    points = []
    for i in range(0,n):
        i = i#dummy just to remove warning
        p = (int(np.random.uniform(0,100)),int(np.random.uniform(0,100)))
        points.append(p)
    return points


# calculates the distance between two points
def distanceBetweenPoints(p1,p2):
    return int(math.sqrt( pow(p1[0]-p2[0],2)  + pow( p1[1] - p2[1],2)   ))


# checks if two lines intersect or not
def doesLinesIntersect(p11,p12,p21,p22):
    line = LineString([p11,p12])
    other = LineString([p21,p22])
    return line.intersects(other)

def validLine(line,allLines):
    valid = True
    for i in allLines:
        if(line.coords[0] != i.coords[0] and line.coords[0] != i.coords[1] and line.coords[1] != i.coords[0] and line.coords[1] != i.coords[1]):
            if line.intersects(i) == True:
                valid = False
                return False
        #else:
            #return True
    return valid

# takes array of points to generate list of cities
def generateCityList(points):
    country = []
    for i in range (len(points)):
        neighbours = []
        neighboursChecked = []
        for j in range (len(points)):
            if(points[j] == points[i]):
                continue
            neighbours.append(j)
            neighboursChecked.append(False)
        city = {
            "id":i,
            "neighbours": neighbours,
            "neighboursChecked":neighboursChecked,
            "pos":points[i],
            "done":False
        }
        country.append(city)
    return country

#given total map (Country) reorder neighbours based on distance
# closest one first
def reorderNeighbourCities(country):
    for x in range(len(country)):
        city = country[x]
        neighbours = []
        neighbours = city["neighbours"]
        distances = []
        for i in neighbours:
            d = distanceBetweenPoints(city['pos'],country[i]['pos'])
            distances.append(d)
            zipped_lists = zip(distances,neighbours)
            sorted_zipped_lists = sorted(zipped_lists)
            sortedNeighbours = [element for _, element in sorted_zipped_lists]
        country[x]["neighbours"] = sortedNeighbours
    return country




def generateFinalMap(country):
    finalMap = []
    allLines = []
    it = 0
    for i in range(len(country)):
        finalMap.append([])
    exitloop = False
    while(not exitloop):
        # pick random city x
        x = random.randrange(len(country))
        city = country[x]
        # if city still not done
        if city["done"] == False:
            for i in range(len(city["neighbours"])):
                # pick next nearset city that wasn't checked yet
                if city["neighboursChecked"][i] == False:
                    # mark checked
                    city["neighboursChecked"][i] = True
                    # get neighbour city
                    nCity = country[city["neighbours"][i]]
                    # check if line can be added
                    #ciytPos = ( city["pos"][0]-2 , city["pos"][1]-2 )
                    #ncityPos = ( nCity["pos"][0]-2 , nCity["pos"][1]-2)
                    line = LineString([ city["pos"] , nCity["pos"] ])
                    valid = validLine(line, allLines)
                    # if line can be added
                    # add to allLines and add to finalMap
                    if valid == True:
                        allLines.append(line)
                        finalMap[city["id"]].append(nCity["id"])
                        #mark checked in neighbour city also
                        finalMap[nCity["id"]].append(city["id"])
                        for j in range(len(nCity["neighbours"])):
                            if nCity["neighbours"][j] == city["id"]:
                                nCity["neighboursChecked"][j] = True
                                break
                    break
                                
        #check if current city is done 
        cityDone = all(city["neighboursChecked"])
        city["done"] = cityDone
        
        # if all cities are done exit
        it += 1
        done = True
        for c in country:
            done = done and c["done"]
        if done == True:
            exitloop = True
    #print("it = ",it)
    return finalMap

                    
                    


def GenerateInput(n):
    points = GenerateNPoints(n)
    country = generateCityList(points)
    country = reorderNeighbourCities(country)
    finalMap = generateFinalMap(country)
    return finalMap,points


'''
n = 50
start = timeit.default_timer()
result = GenerateInput(n)
stop = timeit.default_timer()
print("time = ", stop-start)
'''


'''
points = GenerateNPoints(6)
country = generateCityList(points)
country = reorderNeighbourCities(country)
finalMap = generateFinalMap(country)
print(finalMap)
print(points)
'''