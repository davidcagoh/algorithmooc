# input: adjacency list graph with the first line being the N and M and then each row being (u v weight) basically
# the cost of the overall minimum spanning tree after running prim's algorithm to compute it

# i would need a few functions to keep the code modular
# first: parse graph which will store two entries every time with u,v and v,u to show undirectedness
# second: init_heap which will create a heap from heapdict and make a bunch of entries which are basically all the nodes (unreachable thus infinity weight)
# third: start the algorithm running which initializes a set called visited, a mst_cost called 0, and sets hd[1] to 0 as the arbitrary start, i guess this can all go in main instead of its own modular code
# fourth: prim loop which can honestly just go in main function also, while the heap hd isn't empty we do a BFS style extract min visitation with decrease key updates for all its neighbors in graph, updating mst cost as we go
# return msd cost

from heapdict import heapdict
import sys

def parse_graph(filename):
    with open(filename) as f:
        n, m = map(int, f.readline().split())
        graph = {i: [] for i in range(1, n+1)}
        for line in f:
            u, v, w = map(int, line.split())
            graph[u].append((v, w))
            graph[v].append((u, w))
    return graph, n

def init_heap(n, start=1):
    hd = heapdict()
    for v in range(1, n+1):
        hd[v] = float('inf')
    hd[start] = 0
    return hd

def prim_mst(graph, n, start=1):
    hd = init_heap(n, start)
    visited = set()
    mst_cost = 0

    while hd:
        u, cost = hd.popitem()
        mst_cost += cost
        visited.add(u)
        for v, w in graph[u]:
            if v in hd and w < hd[v]:
                hd[v] = w

    return mst_cost

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python primMST.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    graph, n = parse_graph(filename)
    result = prim_mst(graph, n)
    print("MST cost:", result)
