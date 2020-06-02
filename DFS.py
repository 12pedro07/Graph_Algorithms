import time as t

def __show(graph):
    graph.print_status()
    print()
    
def __visit(u, graph, verbose, wait, time=0):
    u.color = "Gray"
    time += 1
    u.i = time
    for v, _ in u.get_adjacent():
        if verbose:
            __show(graph)
            if wait: t.sleep(3)
        if v.color == "White": time = __visit(v, graph, verbose, wait, time)
    u.color = "Black"
    time += 1
    u.j = time
    return time

def DFS(graph, verbose=True, wait=True):
    time = 0
    graph.reset_graph()
    for u in graph.v:
        if u.color == "White":
            time = __visit(u, graph, verbose, time)
    if verbose:
        __show(graph)
        if wait: t.sleep(3)