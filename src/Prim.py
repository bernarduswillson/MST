from Graph import*
from Utils import*

# node for MST prim
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.weight = 0

# MST prim class
class Prim:
    # initialize MST prim
    def __init__(self, graph):
        self.graph = graph
        self.graph_nodes = graph.nodes
        self.result = []
        self.result = self.search()
        self.cost = self.get_cost(self.result)

    # get adjacent nodes -> list of nodes
    def get_adjacent_nodes(self, node):
        nodes = []
        for n in self.graph_nodes[node.value]:
            adj_node = Node(n)
            nodes.append(adj_node)
        return nodes

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
        # find 2 nodes that have lowest weight
        start = self.get_lowest_edge()
        
        # add start to open nodes
        open_nodes = []
        open_nodes.append(Node(start[0]))
        open_nodes.append(Node(start[1]))

        self.result.append([start[0], start[1]])

        # iterate through open nodes
        while open_nodes:
            all_adj_nodes = []
            # get all adjacent nodes from each open nodes
            for node in open_nodes:
                adj_nodes = self.get_adjacent_nodes(node)
                for adj in adj_nodes:
                    if adj.value in [node.value for node in open_nodes]:
                        continue
                    else:
                        self.update_node(adj, node)
                        all_adj_nodes.append(adj)
            
            # get lowest edge weight from all adjacent nodes
            lowest = None
            for node in all_adj_nodes:
                if lowest is None or node.weight < lowest.weight:
                    lowest = node
            self.result.append([lowest.parent.value, lowest.value])

            # check if all nodes already in mst
            if len(self.result) + 1 == len(self.graph_nodes):
                return self.result

            # make lowest edge weight as new open node
            open_nodes.append(lowest)

    def get_cost(self, result):
        cost = 0
        for edge in result:
            cost += self.graph_nodes[edge[0]][edge[1]]
        return cost