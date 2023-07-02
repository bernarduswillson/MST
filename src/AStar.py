from Graph import*
from Utils import*

# node for a-star
class Node:
    def __init__(self, value):
        self.value = value
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

# a-star class
class AStar:
    # initialize a-star
    def __init__(self, graph, start, goal):
        self.start = Node(start)
        self.goal = Node(goal)
        self.graph = graph
        self.graph_nodes = graph.nodes
        self.open = [self.start]
        self.closed = []
        self.path = []
        self.init_node(self.start)
        self.path = self.search()
        self.cost = self.get_cost(self.path, self.graph_nodes)
        
    # initialize a-star node
    def init_node(self, node):
        node.g = 0
        node.h = self.get_heuristic(node)
        node.f = node.g + node.h
        node.parent = None

    # get heuristic -> int
    def get_heuristic(self, node):
        try :
            return euclidean_distance((self.graph.nodeID[node.value][1], self.graph.nodeID[node.value][2]), (self.graph.nodeID[self.goal.value][1], self.graph.nodeID[self.goal.value][2]))
        except :
            return 0

    # get adjacent nodes -> list of nodes
    def get_adjacent_nodes(self, node):
        nodes = []
        for n in self.graph_nodes[node.value]:
            adj_node = Node(n)
            self.init_node(adj_node)
            nodes.append(adj_node)
        return nodes

    # get lowest f value node -> node
    def get_lowest_f(self):
        lowest = None
        for node in self.open:
            if lowest is None or node.f < lowest.f:
                lowest = node
        return lowest

    # update node attributes (g, h, f, parent)
    def update_node(self, adj, node):
        adj.g = node.g + self.graph_nodes[node.value][adj.value]
        adj.h = self.get_heuristic(adj)
        adj.f = adj.g + adj.h
        adj.parent = node

    # search for path -> list of path nodes
    def search(self):
        # keep searching while there are nodes in the open list
        while len(self.open) > 0:
            # get node with lowest f value
            node = self.get_lowest_f()
            self.open.remove(node)
            self.closed.append(node)

            # check if node is goal
            if node.value == self.goal.value:
                while node is not None:
                    self.path.append(node.value)
                    node = node.parent
                self.path.reverse()
                return self.path
            
            # get adjacent nodes
            adj_nodes = self.get_adjacent_nodes(node)
            for adj_node in adj_nodes:
                # check if node is in closed list
                if adj_node.value in [n.value for n in self.closed]:
                    continue

                # check if node is in open list
                if adj_node.value in [n.value for n in self.open]:
                    if adj_node.g > node.g + self.graph_nodes[node.value][adj_node.value]:
                        self.update_node(adj_node, node)
                        continue

                # if node is not in open or closed list, add it to open list
                self.open.append(adj_node)
                self.update_node(adj_node, node)

        return None

    # get path cost -> int
    def get_cost(self, path, graph):
        total_cost = 0
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i+1]
            for neighbor in graph[node1]:
                if neighbor == node2:
                    total_cost += graph[node1][neighbor]
        return total_cost