import random
from Essentials.graph_class import Graph
import time

def BFS(graph):
    graph.reset_graph()
    Q = [random.choice(graph.v)]
    Q[0].root_distance = 0
    while Q:
        print("Q: ", [x.value for x in Q])
        u = Q[0]
        del Q[0]
        for v in u.get_adjacent():
            if v.color == "White":
                v.color = "Grey"
                v.root_distance = u.root_distance + 1
                v.parent = u
                Q.append(v)
        u.color = "Black"
        time.sleep(1)
