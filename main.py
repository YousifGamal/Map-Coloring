import GenerateMap
import minConflict
import backtracking
import ForwardChecking
import MAC
import sys
import timeit

def litsAverage(l,l2):
    if len(l) == 0 and len(l2) == 0:
        return 0
    return (sum(l)+sum(l2))/(len(l)+len(l2))

def main():
    #Arguments
    if len(sys.argv) == 4:
        runs = int(sys.argv[1]) #number of runs
        n = int(sys.argv[2]) #value for n (size of graph)
        c = int(sys.argv[3])#number of colors
    else:
        print("You are messing some arguments")
        return False
    
    if runs < 1:
        print("Number of runs should be 1 or more")
        return False
    if n < 1:
        print("Grahp size should be 1 or more")
        return False
    if c < 3 or c > 4:
        print("Number of colors used is only 3 or 4")
        return False
    if c == 3:
        colors = ['R','G','B']
    else:
        colors = ['R','G','B','Y']
    maxSteps = pow(n,2)
    if maxSteps < 100:
        maxSteps = 100
    solvedTimes = []
    unsolvedTimes = []
    #each algo has solved times and unsolved times
    for j in range(4):
        solvedTimes.append([])
        unsolvedTimes.append([])
        j=j#dummy for warning
    for i in range(runs):
        i = i#dummy for warning
        #generate graph
        graph, Nodes = GenerateMap.GenerateInput(n)
        if runs == 1:
            print("Cities positions = ",Nodes)
            print("Map = ",graph)
        #print("graph generated")
        #minimum conflicts
        start = timeit.default_timer()
        solved, assignment = minConflict.MinConflicts(n,graph,colors,maxSteps)
        stop = timeit.default_timer()
        if solved:
            solvedTimes[0].append(stop-start)
        else:
            unsolvedTimes[0].append(stop-start)
        if runs == 1:#if one rune only -> print the solution
            print("------Using Min Conflict---------------")
            if solved:
                print("#########Problem solved#############")
                print("City colors in order = ",assignment)
            else:
                print("------------Problem wasn't solved-----------------")
                print("City colors in order = ",assignment)
        #backTracking
        start = timeit.default_timer()
        result = backtracking.initializeBacktracking(n,graph,colors)
        stop = timeit.default_timer()
        if result != False:
            solvedTimes[1].append(stop-start)
        else:
            unsolvedTimes[1].append(stop-start)
        if runs == 1:#if one rune only -> print the solution
            print("------Using backtracking---------------")
            if result != False:
                print("#########Problem solved#############")
                print("City colors in order = ",result)
            else:
                print("############Problem wasn't solved#################")
        #backTracking with forwardchecking
        start = timeit.default_timer()
        result = ForwardChecking.backtrackingWForwardChecking(n,graph,colors)
        stop = timeit.default_timer()
        if result != False:
            solvedTimes[2].append(stop-start)
        else:
            unsolvedTimes[2].append(stop-start)
        if runs == 1:#if one rune only -> print the solution
            print("------Using backtracking with forwardchecking---------------")
            if result != False:
                print("#########Problem solved#############")
                print("City colors in order = ",result)
            else:
                print("############Problem wasn't solved#################")
        #backTracking with MAC
        start = timeit.default_timer()
        result = MAC.backtrackingWMAC(n,graph,colors)
        stop = timeit.default_timer()
        if result != False:
            solvedTimes[3].append(stop-start)
        else:
            unsolvedTimes[3].append(stop-start)
        if runs == 1:#if one rune only -> print the solution
            print("------Using backtracking with MAC---------------")
            if result != False:
                print("#########Problem solved#############")
                print("City colors in order = ",result)
            else:
                print("############Problem wasn't solved#################")
    #end of for loop
    algoNames = ["Min Conflict","Backtracking","Backtracking with Forward Checking",
                    "Backtracking with MAC"]
    for j in range(4):
        print("------------------------------------------------")
        print(algoNames[j])
        print("Number of solved problems = ",len(solvedTimes[j]))
        avg = litsAverage(solvedTimes[j],[])
        print("Average time = ",avg)
        print("Number of unsolved problems = ",len(unsolvedTimes[j]))
        avg = litsAverage(unsolvedTimes[j],[])
        print("Average time = ",avg)
        print("Total Number of problems = ",len(unsolvedTimes[j])+len(solvedTimes[j]))
        avg = litsAverage(solvedTimes[j],unsolvedTimes[j])
        print("Total average time = ", avg)
        print("solved% = ", (len(solvedTimes[j])/(len(solvedTimes[j])+len(unsolvedTimes[j])))*100 )



main()
