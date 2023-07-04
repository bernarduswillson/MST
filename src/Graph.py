from Node import*
from Utils import*

# graph class
class Graph:
    # initialize graph
    def __init__(self):
        self.nodes = {}
        self.Maplat = 0
        self.Maplong = 0
        self.Mapname = ""
        self.Mapzoom = 0
        self.nodeID = {}
        self.numNodes = 0

    # add node to graph    
    def addNode(self,node):
        self.nodes[node.value] = node.neighbors

    # remove node from graph
    def removeNode(self,node):
        if node in self.nodes:
            del self.nodes[node]
        else:
            raise Exception("Node not in graph")
        
        # remove node from neighbors
        for neighbor in self.nodes:
            if node in self.nodes[neighbor]:
                del self.nodes[neighbor][node]

    # create graph from file
    def createGraph(self, filename):
        file = open(filename, 'r')
        file_temp1 = open(filename, 'r')
        file_temp2 = open(filename, 'r')
        i = 1
        
        # check if the matrix is square
        lines = file_temp2.readlines()
        for line in lines:
            if len(line.split()) != len(lines):
                raise Exception("The matrix is not square")
        
        # read file from txt
        for line in file:
            line = line.split()
            for j in range(0, len(line)):
                if line[j] != '0':
                    neighborValue = j + 1
                    weight = float(line[j])
                    node = Node(i)
                    node.addNeighbor(neighborValue, weight)
                    if i not in self.nodes:
                        self.addNode(node)
                    else:
                        self.nodes[i][neighborValue] = weight
            # Add nodes without edges
            if i not in self.nodes:
                node = Node(i)
                self.addNode(node)
            i += 1

    # print graph
    def printGraph(self):
        for node in self.nodes:
            print(node, self.nodes[node])

    # print nodeID
    def printNodeID(self):
        for node in self.nodeID:
            print(node, self.nodeID[node])