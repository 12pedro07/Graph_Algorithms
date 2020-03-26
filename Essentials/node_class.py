from math import inf

class Node():
    def __init__(self, value, adjacent_nodes=()):
        self.value = value
        self.__adjacent_nodes = adjacent_nodes
        self.color = "White"
        self.i = 0
        self.j = 0
        self.build_value = inf

    def add_adjacent(self, node):
        self.__adjacent_nodes += (node, )

    def get_adjacent(self):
        return self.__adjacent_nodes
