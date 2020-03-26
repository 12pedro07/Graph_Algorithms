import math

class Node():
    def __init__(self, value, adjacent_nodes=()):
        self.value = value
        self.parent = None
        self.__adjacent_nodes = adjacent_nodes
        self.color = "White"
        self.i = 0
        self.j = 0
        self.root_distance = math.inf

    def add_adjacent(self, node):
        self.__adjacent_nodes += (node, )

    def get_adjacent(self):
        return self.__adjacent_nodes

    def reset(self):
        self.color = "White"
        self.i = self.j = 0
        self.root_distance = math.inf
        self.parent = None
