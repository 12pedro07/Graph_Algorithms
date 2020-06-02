import heapq

def __Relax(n1, n2, e):
    if n2.distance > n1.distance + e:
        n2.distance = n1.distance + e
        n2.parent = n1

def DIJKSTRA(graph, source):
    graph.reset_graph()
    (graph.v)[source].distance = 0
    # Shortest Path (SP)
    SP = []
    Q = [node for node in graph.v]
    heapq.heapify(Q)
    while len(Q) != 0:
        u = heapq.heappop(Q)
        SP.append(u)
        for vertex, edge in u.get_adjacent():
            __Relax(u, vertex, edge)
    graph.print_status()