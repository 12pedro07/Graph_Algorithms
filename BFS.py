import random
import time

def BFS(graph, first=None, verbose=True, wait=True):
    graph.reset_graph()
    if not first:
        Q = [random.choice(graph.v)]
    else:
        Q = [first]
    Q[0].distance = 0
    while Q:
        if verbose: print("Q: ", [x.value for x in Q])
        u = Q[0]
        del Q[0]
        for v, _ in u.get_adjacent():
            if v.color == "White":
                v.color = "Gray"
                v.distance = u.distance + 1
                v.parent = u
                Q.append(v)
        u.color = "Black"
        if wait: time.sleep(1)
    if verbose: 
        graph.print_status()
