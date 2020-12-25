import random


#radomly assign values to variables
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

#assign a value for the given conflicted variable(var) to minimize number of conflicts
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


#Minimum Conflict algorithm
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



