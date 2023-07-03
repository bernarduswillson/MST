from Graph import*
from Utils import*

# node for MST kruskal
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.weight = 0

# MST kruskal class
class Kruskal:
    # initialize MST kruskal
    def __init__(self, graph):
        self.graph = graph
        self.graph_nodes = graph.nodes
        self.result = []
        self.result = self.search()
        self.cost = self.get_cost(self.result)

    # get lowest edge weight -> tuple of node
    def get_lowest_edge(self):
        lowest = None
        for node in self.graph_nodes:
            for neighbor, weight in self.graph_nodes[node].items():
                if lowest is None or weight < lowest[2]:
                    lowest = (node, neighbor, weight)
        return lowest[0], lowest[1]

    # update node attributes (parent)
    def update_node(self, adj, node):
        adj.parent = node
        adj.weight = self.graph_nodes[node.value][adj.value]

    # search for MST -> list of MST edges
    def search(self):
        # sort edges by weight
        edges = []
        for node in self.graph_nodes:
            for neighbor, weight in self.graph_nodes[node].items():
                if (neighbor, node, weight) not in edges:
                    edges.append((node, neighbor, weight))
        edges.sort(key=lambda x: x[2])

        edges_objects = []

        # convert nodes to node objects
        for edge in edges:
            parent = Node(edge[0])
            node = Node(edge[1])
            self.update_node(node, parent)
            edges_objects.append((node, edge[0], edge[1]))

        result = []

        # Union-Find data structure for cycle detection
        sets = {}
        for node in self.graph_nodes:
            sets[node] = Node(node)

        # iterate through edges
        for edge in edges_objects:
            node, node1, node2 = edge

            # find the sets to which the nodes belong
            set1 = self.find_set(sets, node1)
            set2 = self.find_set(sets, node2)

            # check if adding the edge creates a cycle
            if set1 != set2:
                result.append([node1, node2])
                self.union(sets, set1, set2)

        return result

    # find the set to which a node belongs (with path compression)
    def find_set(self, sets, node):
        if sets[node].parent is None:
            return node
        sets[node].parent = self.find_set(sets, sets[node].parent)
        return sets[node].parent

    # merge two sets
    def union(self, sets, set1, set2):
        sets[set2].parent = set1

    def get_cost(self, result):
        cost = 0
        for edge in result:
            cost += self.graph_nodes[edge[0]][edge[1]]
        return cost