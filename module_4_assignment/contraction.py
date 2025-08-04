# input: a txt file with an adjacency list which is a bunch of rows where the first column is the vertex number
# and the rest of the columns are the vertices that the vertex has an undirected edge with.
# output: the min cut of the graph after some iterations of the algorithm (n^2 ln n iterations to be precise, for which 
# we have a guarantee that the min cut is returned with probability 1/n

import sys
import math

def parse_graph(filepath):
    edges = set()
    with open(filepath, 'r') as f:
        for line in f:
            parts = list(map(int, line.strip().split()))
            u = parts[0]
            # print("starting ", u)
            for v in parts[1:]:
                if u < v:  # to avoid duplicate undirected edges
                    edges.add((u, v))
                    # print("added edge",u, ", ", v)
                else:
                    edges.add((v, u))
                    # print("added edge",v, ", ", u)
    return list(edges)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 contraction.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    edges = sorted(parse_graph(filepath))
    for edge in edges[:10]:
        print(edge)
    # print(edges[100])
    # set seed as 1234
    best_cut = contract(G, seed)
    # have a array of n^2 log n seeds here and we're given that n is 200 so that's 211933 seeds
    # for seed in seed array, run contract and update best_cut if best_cut is smaller

    print(best_cut)

def contract(G, seed):
    # if it has 2 vertices, 
    #   return cut, the number of edges coming out of the first vertex (which is between them)
    # else, 
    #   pick an edge (u,v) with uniform random probability
    #   update G by merge the two vertices into some supernode w 
    #   update G by remove self loops: rows where the row number appears there too
    #   cut equals recursively run contract on updated G with the same seed
    return cut

def merge(G, u,v):
    # basically add everything coming out of node v into the row that denotes edges coming out of node u
    # then go through the whole graph representation and when you come across a link to node v, replace it with node u
    # return the new G
    return G
