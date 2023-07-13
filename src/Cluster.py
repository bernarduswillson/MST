from Kruskal import*
from Prim import*

class Cluster:
    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        self.result = self.search()
        self.clusters = self.clusters()

    # remove largest weight edge
    def search(self):
        kruskal = Kruskal(self.graph)
        result = kruskal.result
        for i in range(self.n - 1):
            result.pop()
        return result
    
    # get clusters
    def clusters(self):
        clusters = []
        for pair in self.result:
            found_clusters = []
            for i, cluster in enumerate(clusters):
                if pair[0] in cluster or pair[1] in cluster:
                    found_clusters.append(i)
            if not found_clusters:
                clusters.append(set(pair))
            else:
                new_cluster = set(pair)
                for idx in sorted(found_clusters, reverse=True):
                    new_cluster.update(clusters.pop(idx))
                clusters.append(new_cluster)
        return [list(cluster) for cluster in clusters]

