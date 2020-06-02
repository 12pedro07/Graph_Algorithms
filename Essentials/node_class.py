import math

class Node():
    def __init__(self, value, adjacent_nodes=()):
        self.value = value
        self.parent = None
        self.__adjacent_nodes = adjacent_nodes
        self.color = "White"
        self.i = 0
        self.j = 0
        self.distance = math.inf

    def add_adjacent(self, node, value):
        self.__adjacent_nodes += ([node, value], )

    def get_adjacent(self):
        return self.__adjacent_nodes

    def reset(self):
        self.color = "White"
        self.i = self.j = 0
        self.distance = math.inf
        self.parent = None

    def __lt__(self, other):
        if self.distance < other.distance:
            return self
        return other
        
    def __gt__(self, other):
        if self.distance > other.distance:
            return self
        return other  

    def __str__(self):
        parentValue = None if not self.parent else self.parent.value
        return "{}\t-\t{}\t-\t{}\t-\t({}|{})\t-\t{}".format(
            self.value, self.color, self.distance,
            self.i,self.j,
            parentValue)