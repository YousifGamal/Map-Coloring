import GenerateMap
import minConflict
import backtracking
import ForwardChecking
import MAC
import sys
import timeit

def litsAverage(l):
    if(len(l) == 0):
        return 0
    return sum(l)/len(l)

def main():
    #Arguments
    if len(sys.argv) == 5:
        runs = int(sys.argv[1]) #number of runs
        n = int(sys.argv[2]) #value for n (size of graph)
        algo = int(sys.argv[3])#the wanted algorithm 
        c = int(sys.argv[4])#number of colors
    else:
        print("You are messing some arguments")
        return False
    
    if runs < 1:
        print("Number of runs should be 1 or more")
        return False
    if n < 1:
        print("Grahp size should be 1 or more")
        return False
    if algo < 1 or algo > 4:
        print("Algos are numbered from 1 to 4")
        return False
    if c < 3 or c > 4:
        print("Number of colors used is only 3 or 4")
        return False
    if c == 3:
        colors = ['R','G','B']
    else:
        colors = ['R','G','B','Y']
    maxSteps = 1000
    solvedTimes = []
    unsolvedTimes = []
    for i in range(runs):
        i = i#dummy for warning
        #generate graph
        graph, Nodes = GenerateMap.GenerateInput(n)
        print("graph generated")
        #if minimum conflicts
        if algo == 1:
            start = timeit.default_timer()
            solved, assignment = minConflict.MinConflicts(n,graph,colors,maxSteps)
            stop = timeit.default_timer()
            if solved:
                solvedTimes.append(stop-start)
            else:
                unsolvedTimes.append(stop-start)
            if runs == 1:#if one rune only -> print the solution
                if solved:
                    print("#########Problem solved#############")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
                    print("City colors in order = ",assignment)
                else:
                    print("------------Problem wasn't solved-----------------")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
                    print("City colors in order = ",assignment)
        elif algo == 2: #backTracking
            start = timeit.default_timer()
            result = backtracking.initializeBacktracking(n,graph,colors)
            stop = timeit.default_timer()
            if result != False:
                solvedTimes.append(stop-start)
            else:
                unsolvedTimes.append(stop-start)
            if runs == 1:#if one rune only -> print the solution
                if result != False:
                    print("#########Problem solved#############")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
                    print("City colors in order = ",result)
                else:
                    print("############Problem wasn't solved#################")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
        elif algo == 3: #backTracking with forwardchecking
            start = timeit.default_timer()
            result = ForwardChecking.backtrackingWForwardChecking(n,graph,colors)
            stop = timeit.default_timer()
            if result != False:
                solvedTimes.append(stop-start)
            else:
                unsolvedTimes.append(stop-start)
            if runs == 1:#if one rune only -> print the solution
                if result != False:
                    print("#########Problem solved#############")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
                    print("City colors in order = ",result)
                else:
                    print("############Problem wasn't solved#################")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
        elif algo == 4: #backTracking with MAC
            start = timeit.default_timer()
            result = MAC.backtrackingWMAC(n,graph,colors)
            stop = timeit.default_timer()
            if result != False:
                solvedTimes.append(stop-start)
            else:
                unsolvedTimes.append(stop-start)
            if runs == 1:#if one rune only -> print the solution
                if result != False:
                    print("#########Problem solved#############")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
                    print("City colors in order = ",result)
                else:
                    print("############Problem wasn't solved#################")
                    print("Cities positions = ",Nodes)
                    print("Map = ",graph)
    #end of for loop
    print("------------------------------------------------")
    print("Number of solved problems = ",len(solvedTimes))
    avg = litsAverage(solvedTimes)
    print("Average time = ",avg)
    print("------------------------------------------------")
    print("Number of unsolved problems = ",len(unsolvedTimes))
    avg = litsAverage(unsolvedTimes)
    print("Average time = ",avg)

main()
