from BFS import BFS
from DFS import DFS
from PRIM import PRIM
from KRUSKAL import KRUSKAL
from DIJKSTRA import DIJKSTRA
from BELLMAN_FORD import BELLMAN_FORD
from Essentials.graph_class import Graph

print(">>> BFS <<<")
#              v  r  s  w  t  x  u  y
adj_matrix = [[0, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 1, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 1, 1, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 1, 0]]
gBFS = Graph(adj_matrix,['v','r','s','w','t','x','u','y'])
BFS(gBFS,first=gBFS.v[2], verbose=False, wait=False)
gBFS.print_status()

print("-"*80)
print("\n>>> DFS <<<")
#              a  b  c  d  e  f  g  h
adj_matrix = [[0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
gDFS = Graph(adj_matrix,['a','b','c','d','e','f','g','h'])
DFS(gDFS,verbose=False,wait=False)
gDFS.print_status()

print("-"*80)
print("\n>>> Prim <<<")
#              a   b   c   d   e   f   g   h
adj_matrix = [[0,  6,  5,  0,  14, 10, 0,  0],
              [6,  0,  4,  0,  0,  0,  0,  0],
              [5,  4,  0,  9,  0,  0,  2,  0],
              [0,  0,  9,  0,  0,  0,  0,  0],
              [14, 0,  0,  0,  0,  3,  0,  0],
              [10, 0,  0,  0,  3,  0,  8,  0],
              [0,  0,  2,  0,  0,  8,  0,  15],
              [0,  0,  0,  0,  0,  0,  15, 0]]
gPrim = Graph(adj_matrix,['a','b','c','d','e','f','g','h'])
PRIM(gPrim,4)

print("-"*80)
print("\n>>> Kruskal <<<")
#              a   b   c   d   e   f   g   h
adj_matrix = [[0,  6,  5,  0,  14, 10, 0,  0],
              [6,  0,  4,  0,  0,  0,  0,  0],
              [5,  4,  0,  9,  0,  0,  2,  0],
              [0,  0,  9,  0,  0,  0,  0,  0],
              [14, 0,  0,  0,  0,  3,  0,  0],
              [10, 0,  0,  0,  3,  0,  8,  0],
              [0,  0,  2,  0,  0,  8,  0,  15],
              [0,  0,  0,  0,  0,  0,  15, 0]]
gKruskal = Graph(adj_matrix,['a','b','c','d','e','f','g','h'])
KRUSKAL(gKruskal)

print("-"*80)
print("\n>>> Dijkstra <<<")
#              s   u   v   x   y
adj_matrix = [[0,  10, 0,  5,  0],
              [0,  0,  1,  2,  0],
              [0,  0,  0,  0,  4],
              [0,  3,  9,  0,  2],
              [7,  0,  6,  0,  0]]
gDijkstra = Graph(adj_matrix,['s','u','v','x','y'])
DIJKSTRA(gDijkstra, 0)

print("-"*80)
print("\n>>> BELLMAN-FORD <<<")
#              a   b   c   d
adj_matrix = [[0, 20,  0,  0],
              [0,  0,  2,  0],
              [0,  0,  0,  1],
              [2, -5,  0,  0]]
gBellmanFord = Graph(adj_matrix,['a','b','c','d'])
message = "No negative loops" if BELLMAN_FORD(gBellmanFord, 0) else "Negative loop found"
print(message)
gBellmanFord.print_status()