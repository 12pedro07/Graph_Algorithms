import random

def __Make_Set(graph):
    # i = initial set value
    # j = current set value
    value_set = [i for i in range(len(graph.v))]
    random.shuffle(value_set)
    for node, value in zip(graph.v,value_set):
        node.i = node.j = value
        node.parent = node
        
def __Find_Set(node):
    current = node
    while current.parent != current:
        current = current.parent
    return current

def __Union(n1,n2):
    n2.parent = n1

def KRUSKAL(graph):
    graph.reset_graph()
    # make a set of diferent numbers for each node
    __Make_Set(graph)
    # sort by min edge value
    e = graph.e.copy()
    e.sort(key = lambda x: x[2])
    # look at all edges
    for n1,n2,_ in e:
        # if the vertices have diferent values, update
        if __Find_Set(n1) != __Find_Set(n2):
            __Union(__Find_Set(n1), __Find_Set(n2))
    
    # end updating set values (display purposes only)
    for node in graph.v:
        node.j = __Find_Set(node).j
    
    graph.print_status()