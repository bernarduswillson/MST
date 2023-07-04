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

    # remove node from file
    def remove_node_file(self, filename, node):
        with open(filename, 'r') as file:
            lines = file.readlines()

        matrix = []
        for line in lines:
            values = list(map(int, line.split()))
            matrix.append(values)

          # set the all values in the node's row and column to 0
        for i in range(len(matrix)):
            matrix[i][node - 1] = 0
            matrix[node - 1][i] = 0

        with open(filename, 'w') as file:
            for row in matrix:
                new_line = ' '.join(map(str, row)) + '\n'
                file.write(new_line)

    # add edge from file
    def add_edge_file(self, filename, node1, node2, weight):
        with open(filename, 'r') as file:
            lines = file.readlines()

        matrix = []
        for line in lines:
            values = list(map(int, line.split()))
            matrix.append(values)

        # if node1 or node 2 larger than matrix size
        if node1 > len(matrix) or node2 > len(matrix):
            while node1 > len(matrix) or node2 > len(matrix):
                matrix.append([0] * len(matrix))
                for i in range(len(matrix)):
                    matrix[i].append(0)

        # set the values in the node's row and column to weight
        matrix[node1 - 1][node2 - 1] = weight
        matrix[node2 - 1][node1 - 1] = weight

        with open(filename, 'w') as file:
            for row in matrix:
                new_line = ' '.join(map(str, row)) + '\n'
                file.write(new_line)

    # remove edge from file
    def remove_edge_file(self, filename, node1, node2):
        with open(filename, 'r') as file:
            lines = file.readlines()

        matrix = []
        for line in lines:
            values = list(map(int, line.split()))
            matrix.append(values)

        # set the values in the node's row and column to 0
        matrix[node1 - 1][node2 - 1] = 0
        matrix[node2 - 1][node1 - 1] = 0

        with open(filename, 'w') as file:
            for row in matrix:
                new_line = ' '.join(map(str, row)) + '\n'
                file.write(new_line)

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