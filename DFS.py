from Essentials.graph_class import Graph

def __visit(u, time=0):
    u.color = "Grey"
    time += 1
    u.i = time
    for v in u.get_adjacent():
        if v.color == "White": time = __visit(v, time)
    u.color = "Black"
    time += 1
    u.j = time
    return time

def DFS(graph):
    time = 0
    graph.reset_graph()
    for u in graph.v:
        if u.color == "White":
            time = __visit(u,time)
