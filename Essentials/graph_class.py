from .node_class import Node

class Graph():
    def __init__(self, adj_matrix, node_values):
        self.adj_matrix = adj_matrix
        self.node_values = node_values
        # check if node_values is valid
        if len(adj_matrix) != len(node_values):
            raise Exception("Incompatible sizes exception")

        # instanciate all nodes
        self.v = tuple([ Node(node_values[i]) for i in range(len(adj_matrix))])

        for adj_nodes, node in zip(adj_matrix, self.v):
            for idx, n in enumerate(adj_nodes):
                if n > 0: node.add_adjacent(self.v[idx])

    def __str__(self):
        for item in self.v:
            print("Node: ", item.value)
            print("\t- Parent: {}".format(item.parent.value if item.parent else "<empty>"))
            print("\t- Color: {}".format(item.color))
            print("\t- i|j: {}|{}".format(item.i, item.j))
            print("\t- Root distance: {}".format(item.root_distance))
            print("\t- Adjacents: {}".format( [val.value for val in item.get_adjacent()] ))
            print("="*70)
        return ""

    def reset_graph(self):
        for item in self.v: item.reset()
