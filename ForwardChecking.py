import GenerateMap
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


def forwardChecking(assignment, domain, graph, var):
    neighbours = graph[var]
    value = assignment[var]
    #for all neighbours
    for n in neighbours:
        if assignment[n] == -1:#unassigned neighbour
            #remove the assigned value of the var from the neighbours of the var
            if value in domain[n]:#if value is in the neighbour domain
                domain[n].remove(value)#remove vlaue from neighbour domain
                if len(domain[n]) == 0:#domain of neighbor became empty return false
                    return False
    return domain




#recursive function for backTracking
def backtrackingWFwdChkUtility(graph, assignment, domain ,var):
    if completeAssignmet(assignment):
        return assignment
    for i in range(len(domain[var])):#for current var select a value from its domain
        assignment[var] = domain[var][i]#assign the value
        oldDomain = domain
        if consistentAssignment(assignment,graph,var):#check if assignmet consistent
            #apply forward checking
            oldDomain = copy.deepcopy(domain)
            domain = forwardChecking(assignment,domain,graph,var)
            if domain != False:  
                result = backtrackingWFwdChkUtility(graph, assignment, domain, var+1)
                if result != False:
                    return result
        assignment[var] = -1
        domain = oldDomain
    return False




#initialzie all nodes with invalid assignmet = -1
#all vars domain is the same (all colors)
#and start the algorithm
def backtrackingWForwardChecking(n,graph,colors):
    assignment = []
    domain = []
    for i in range(n):
        assignment.append(-1)
        i = i#dummy assignment for the warning
        domain.append(copy.deepcopy(colors))
    return backtrackingWFwdChkUtility(graph,assignment,domain,0)



'''
graph = [[1,5],
            [2,0,5],
            [1,3,5],
            [2,4,5],
            [3,5],
            [0,1,2,3,4],
            ]
'''
'''
colors = ['R','G','B','Y']
n=8

graph, Nodes = GenerateMap.GenerateInput(n)
result = backtrackingWForwardChecking(n,graph,colors)
if result != False:
    print("#########Problem solved#############")
    print("Cities positions = ",Nodes)
    print("Map = ",graph)
    print("City colors in order = ",result)
else:
    print("------------Problem wasn't solved-----------------")
    print("Cities positions = ",Nodes)
    print("Map = ",graph)

'''