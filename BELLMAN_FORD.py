def __Relax(n1, n2, e):
    if n2.distance > n1.distance + e:
        n2.distance = n1.distance + e
        n2.parent = n1

def BELLMAN_FORD(graph, source):
    graph.reset_graph()
    (graph.v)[source].distance = 0
    for i in range(1,len(graph.v)):
        for n1,n2,edge in graph.e:
            __Relax(n1,n2,edge)
    for n1,n2,edge in graph.e:
        if n2.distance > n1.distance + edge:
            return False
    return True