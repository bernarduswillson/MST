# node class
class Node:
    # initialize node
    def __init__(self,value):
        self.value = value
        self.neighbors = {}    
    
    # add neighbor to node
    def addNeighbor(self,neighborValue,weight):
        self.neighbors[neighborValue] = weight