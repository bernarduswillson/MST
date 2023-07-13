from Graph import*
from Prim import*
from Kruskal import*
from Cluster import*

G = Graph()
G.createGraph("test/map2.txt")
G.printGraph()

# PRIM
print("\nPRIM")
prim = Prim(G)
print("MST: ", prim.result)

# KRUSKAL
print("\nKRUSKAL")
kruskal = Kruskal(G)
print("MST: ", kruskal.result)

# CLUSTER
print("\nCLUSTER")
cluster = Cluster(G, 2)
print("Result: ", cluster.search())
for i, cluster in enumerate(cluster.clusters):
    print("Cluster", i + 1, ": ", cluster)
