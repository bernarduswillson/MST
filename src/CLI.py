from Graph import*
from Prim import*
from Kruskal import*
from Cluster import*
import time

G = Graph()
G.createGraph("test/tes.txt")
G.printGraph()
start = 1
goal = 5

# PRIM
print("\nPRIM")
startTime = time.perf_counter_ns()
prim = Prim(G)
endTime = time.perf_counter_ns()
print("MST: ", prim.result)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

# KRUSKAL
print("\nKRUSKAL")
startTime = time.perf_counter_ns()
kruskal = Kruskal(G)
endTime = time.perf_counter_ns()
print("MST: ", kruskal.result)
# print("Total Cost: ", kruskal.cost)
runtime = (endTime - startTime) / 1000
print("Runtime: {:.2f} ms".format(runtime))

# CLUSTER
print("\nCLUSTER")
clusters = mst_based_clustering(kruskal.result, 2)
print("Clusters: ", clusters)