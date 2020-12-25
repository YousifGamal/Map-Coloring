import copy
#checks if current assignment is consistent 
def consistentAssignment(assignment,graph,var):
    # get neighbours of var in the graph
    neighbours = graph[var]
    for neighbour in neighbours:#check for all neighbours of given var
        #if valid assignment != -1 and var and its neighbour both are equal then not consistent assignmet
        if assignment[neighbour] != -1 and assignment[neighbour] == assignment[var]:
            return False
    return True

#if complete assignemt then problem solved
def completeAssignmet(assignmet):
    for i in assignmet:
        if i == -1:# if any value is not assigned (= -1) then not complete assignemt 
            return False
    return True

#MAC function
def MAC(assignment, domain, graph, i):
    neighbours = graph[i]#neighbours of Xi
    #for all neighbours
    queue = []
    for n in neighbours:
        if assignment[n] == -1:#unassigned neighbour
            newArc = (n,i)#add the neighbour arc to the initial queue
            queue.append(newArc)
    return MAC_AC_3(queue, domain, graph, assignment)

#AC-3 algorithm but with MAC initial queue
def MAC_AC_3(queue, domain,graph, assignment):
    while len(queue) > 0:#while queue not empty
        arc = queue.pop(0)#remove first arc
        i = arc[0]
        j = arc[1]
        if Revise(domain,graph,arc):#apply arc consistency
            if len(domain[i]) == 0:#check if domaniI is empty
                return False
            neighbours = graph[i]#{unassigned neighbours of I} - j
            for n in neighbours:
                #if n != j:
                if assignment[n] == -1 and n != j:
                    newArc = (n,i)
                    queue.append(newArc)
        return True


#Revise the domin if needed - Utility func for AC-3 
def Revise(domain, graph, arc):
    revised = False
    domainI = domain[arc[0]]
    domainJ = domain[arc[1]]
    dIlenght = len(domainI)
    z = 0
    while z < dIlenght:
        x = domainI[z]
        if checkBinaryConstraint(domainJ,x):#if violates binary constraint
            #remove x from the domain of Xi
            domainI.remove(x)
            revised = True
            z-=1 
            dIlenght -= 1
        z+=1
    return revised



#return true if violates binary constraint 
def checkBinaryConstraint(domainJ,x):
    #get length of domain J
    length = len(domainJ)
    #check for x if in domain j
    if x in domainJ:
        length-=1
    #check if there is no y that can be aassigned
    if length <= 0:    #return true
        return True
    else:
        return False
    
    



#recursive function for backTracking
def backtrackingWMACUtility(graph, assignment, domain ,var):
    if completeAssignmet(assignment):
        return assignment
    for i in range(len(domain[var])):#for current var select a value from its domain
        assignment[var] = domain[var][i]#assign the value
        oldDomain = domain
        if consistentAssignment(assignment,graph,var):#check if assignmet consistent
            #apply forward checking
            oldDomain = copy.deepcopy(domain)
            macResult = MAC(assignment,domain,graph,var)
            if macResult != False:  
                result = backtrackingWMACUtility(graph, assignment, domain, var+1)
                if result != False:
                    return result
        assignment[var] = -1
        domain = oldDomain
    return False






#Backtracking with MAC algorithm
def backtrackingWMAC(n,graph,colors):
    assignment = []
    domain = []
    for i in range(n):
        #initialzie all nodes with invalid assignmet = -1
        assignment.append(-1)
        i = i#dummy assignment for the warning
        #all vars have the same initial domain 
        domain.append(copy.deepcopy(colors))
    #start the algorithm
    return backtrackingWMACUtility(graph,assignment,domain,0)



