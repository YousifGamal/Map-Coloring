import GenerateMap
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

#recursive function for backTracking
def backtracking(graph, assignment, colors, var):
    if completeAssignmet(assignment):
        return assignment
    for i in range(len(colors)):#for current var select consistent assignmet
        assignment[var] = colors[i]
        if consistentAssignment(assignment,graph,var):
            result = backtracking(graph, assignment, colors, var+1)
            if result != False:
                return result
        assignment[var] = -1
    return False


#Backtracking Algorithm
def initializeBacktracking(n,graph,colors):
    assignment = []
    #initialzie all nodes with invalid assignmet = -1
    for i in range(n):
        assignment.append(-1)
        i = i#dummy assignment for the warning
    #start the algorithm
    return backtracking(graph,assignment,colors,0)




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
colors = ['R','G','B']
n=9
graph, Nodes = GenerateMap.GenerateInput(n)
graph =  [[3, 2, 5], [3, 2, 8], [3, 8, 1, 7, 4, 0, 5], [0, 1, 2, 8], 
            [7, 8, 6, 2], [7, 2, 6, 0], [4, 7, 5], [4, 5, 6, 2], [4, 2, 1, 3]]
result = initializeBacktracking(n,graph,colors)
if result != False:
    print("#########Problem solved#############")
    print("Cities positions = ",Nodes)
    print("Map = ",graph)
    print("City colors in order = ",result)
else:
    print("############Problem wasn't solved#################")
    print("Cities positions = ",Nodes)
    print("Map = ",graph)

'''