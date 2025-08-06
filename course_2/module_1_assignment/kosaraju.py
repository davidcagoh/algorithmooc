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
    (1, 2), (2, 4), (4, 1), (4, 3), (3, 5)
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

def kosaraju_scc(edges, num_nodes):
    G, G_rev = build_graph(edges,num_nodes)
    finishing_order = first_pass_loop(G_rev, num_nodes)
    print(finishing_order)
    # scc_sizes = second_pass_loop(G, num_nodes, finishing_order)
                                 
    # scc_sizes.sort(reverse=True)
    # while len(scc_sizes) < 5:
    #     scc_sizes.append(0)
    # return scc_sizes[:5]


def first_pass_loop(G_rev, num_nodes):
    explored = set()
    finishing_order = []
    finished = defaultdict(bool)
    # First pass: on reversed graph
    for node in range(num_nodes, 0, -1):
        if node not in explored:
            dfs_iterative_first_pass(G_rev, node, explored, finishing_order, finished)
    return finishing_order

def dfs_iterative_first_pass(G_rev, start, explored, finishing_order, finished):
    stack = [start]
    while stack:
        node = stack[-1]
        if node not in explored:
            explored.add(node)
            # Push neighbors
            for nei in sorted(G_rev[node], reverse=True):
                if nei not in explored:
                    stack.append(nei)
        else:
            stack.pop()
            if not finished[node]:
                finished[node] = True
                finishing_order.append(node)

kosaraju_scc(edges,num_nodes)

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

