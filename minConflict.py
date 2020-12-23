import random
import GenerateMap

def intilaizeCSP(n, colors):
    assignment = []
    for i in range(n):
        # pick random color to assign to a city
        randomColorIndex = random.randrange(len(colors))
        assignment.append(colors[randomColorIndex])
        i = i#dummy just to remove warning
    return assignment

#count the total number of conflicts
def conflicts(assignment,finalMap):
    totalConflicts = 0
    eachVarConflict = []
    for i in range(len(finalMap)):#for each node
        localConflict = 0
        for j in range(len(finalMap[i])):# For every neighbour to that node
            if assignment[i] == assignment[finalMap[i][j]]:#check if conflict present
                totalConflicts += 1
                localConflict += 1
        eachVarConflict.append(localConflict)
    return totalConflicts, eachVarConflict

#assign a value for the given variable(var) to minimize number of conflicts
def minimizeConflict(var,assignment,finalMap,colors):
    currentConflicts, eachVarConflict = conflicts(assignment,finalMap)
    oldColor = assignment[var]# old color so we don't do reduntant check
    value = assignment[var]# new value to be assigned
    for i in range(len(colors)):# for every color availabe
        if oldColor != colors[i]:#if old color not equal new color
            assignment[var] = colors[i]# assign the new color
            newConflicts, eachVarConflict = conflicts(assignment,finalMap)#calc new number of conflict
            if newConflicts < currentConflicts:# if new less than old choose this color as the new value
                currentConflicts = newConflicts
                value = colors[i]
    assignment[var] = value



def MinConflicts(n,finalMap,colors,maxSteps):
    assignemt = intilaizeCSP(n,colors)
    for i in range(maxSteps):
        i = i#dummy just to remove warning
        currrentConflicts , eachVarConflict = conflicts(assignemt,finalMap)
        if currrentConflicts == 0:#CSP solved
            return True, assignemt
        #pick random conflicted node to change its color
        picked = False
        while not picked:
            #pick random node number 
            randomNodeNumber = random.randrange(n)
            #check if it's conflicted or not
            if eachVarConflict[randomNodeNumber] > 0:
                picked = True
        #pick new value to minimize conflicts
        minimizeConflict(randomNodeNumber,assignemt,finalMap,colors)
    # after reaching max steps
    #check if solved or not
    currrentConflicts, eachVarConflict = conflicts(assignemt,finalMap)
    if currrentConflicts == 0:#CSP solved
            return True, assignemt
    else:
        return False, assignemt




#dummy data

'''
finalMap = [[1,5],
            [2,0,5],
            [1,3,5],
            [2,4,5],
            [3,5],
            [0,1,2,3,4],
            ]
# 0->R, 1->G, 0->B,
'''
'''
colors = ['R','G','B'] 
n = 5
maxSteps = 100

finalMap, Nodes = GenerateMap.GenerateInput(n)
solved, assignment = MinConflicts(n,finalMap,colors,maxSteps)
print("GD3ANA")
if solved:
    print("#########Problem solved#############")
    print("Cities positions = ",Nodes)
    print("Map = ",finalMap)
    print("City colors in order = ",assignment)
else:
    print("------------Problem wasn't solved-----------------")
    print("Cities positions = ",Nodes)
    print("Map = ",finalMap)
    print("City colors in order = ",assignment)
'''