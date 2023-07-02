from Graph import*
from AStar import*
from UCS import*
from Prim import*
from Utils import*
import time
import gmplot

G = Graph()
G.createGraph("test/ppt.txt")
G.printGraph()
start = 1
goal = 5

# UCS
print("\nUNIFORM COST SEARCH")
startTime = time.perf_counter_ns()
ucs = UCS(G, start, goal)
endTime = time.perf_counter_ns()
print("Path: ", ucs.path)
print("Total Cost: ", ucs.cost)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

# ASTAR
print("\nA STAR")
startTime = time.perf_counter_ns()
astar = AStar(G, start, goal)
endTime = time.perf_counter_ns()
print("Path: ", astar.path)
print("Total Cost: ", astar.cost)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

# PRIM
print("\nPRIM")
startTime = time.perf_counter_ns()
prim = Prim(G)
endTime = time.perf_counter_ns()
print("MST: ", prim.result)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))