# input: adjacency list representation of G with n = 875000
# output: sizes of 5 largest SCCs in decreasing order

# basic pseudocode
# run DFS-loop subroutine on reversed edges of graph to apply finishing times to every vertex
# run DFS-loop on the graph again but start from the largest finishing times

import sys
from collections import defaultdict


def parse_graph(filepath):
    with open(filepath, 'r') as f:
        edges = [int(line.strip()) for line in f if line.strip()]    
    return edges

edges = [
    (1, 2), (2, 3), (3, 1), (3, 4), (4, 5)
]
num_nodes = 5

def build_graph(edges, num_nodes):
    G = defaultdict(list)
    G_rev = defaultdict(list)
    for tail, head in edges:
        G[tail].append(head)
        G_rev[head].append(tail)
    # Ensure all nodes exist in both graphs
    for node in range(1, num_nodes + 1):
        G[node]
        G_rev[node]
    return G, G_rev

print(build_graph(edges, num_nodes))    


def first_pass_loop(G_rev, nodes):
    explored = set()
    finishing_times = {}
    finishing_order = []
    t = [0]
    for node in sorted(nodes, reverse=True):
        if node not in explored:
            dfs_first_pass(G_rev, node, explored, finishing_times, t, finishing_order)
    return finishing_times, finishing_order

def dfs_first_pass(G_rev, node, explored, finishing_times, t, finishing_order):
    explored.add(node)
    for nei in sorted(G_rev.get(node, []), reverse=True):
        if nei not in explored:
            dfs_first_pass(G_rev, nei, explored, finishing_times, t, finishing_order)
    t[0] += 1
    finishing_times[node] = t[0]
    finishing_order.append(node)


# ftimes, order = first_pass_loop(G_rev, nodes)
# print("Finishing times:", ftimes)
# print("Finishing order:", order)

# basically starting from node n, you DFS it and label finishing times on the way out. 
# i think after the above is done i would want to check with toy examples if the labelling of finishing times works properly
# later on we have to run DFS loop again on the graph but in the decreasing order of finishing times?
# then after everything we have to add bookkeeping code to keep track of the sizes of all the strongly connected components
# i wonder how to manage the modularity of the code; should i make multiple similar subroutines dealing with reversed edges or something to avoid having to duplicate G?

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python3 quickSort.py <input_file>")
#         sys.exit(1)
#     filepath = sys.argv[1]
#     edges = parse_graph(filepath)
#     G, G_rev = build_graph(edges)    
# sizes = main()
#     print(sizes)

