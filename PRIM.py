def __Extract_Min(queue):
    # assume first as minimum distance
    lowest = [0, queue[0].distance]
    # compair until find the lowest distance
    for idx, node in enumerate(queue):
        if node.distance < lowest[1]:
            lowest = [idx, node.distance]
    # pop it from the queue and return
    return queue.pop(lowest[0])

def PRIM(graph, root):
    graph.reset_graph()
    # Queue up all the nodes
    queue = [node for node in graph.v]
    # Initialize root
    queue[root].distance = 0
    # Don't stop until the queue is empty
    while(len(queue) != 0):
        # Remove the lowest valued node
        u = __Extract_Min(queue)
        # Iterate throught the adjacents
        for vertex, edge in u.get_adjacent():
            # check if the distance for this path is lower
            if vertex in queue and edge < vertex.distance:
                # update
                vertex.parent = u
                vertex.distance = edge
    graph.print_status()