# input: a txt file with an adjacency list which is a bunch of rows where the first column is the vertex number
# and the rest of the columns are the vertices that the vertex has an undirected edge with.
# output: the min cut of the graph after some iterations of the algorithm (n^2 ln n iterations to be precise, for which 
# we have a guarantee that the min cut is returned with probability 1/n

import sys
import math
import random

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

def contract(G, seed):
    random.seed(seed)
    vertices = set() # check how many vertices there are
    for u, v in G:
        vertices.add(u)
        vertices.add(v)

    while len(vertices) > 2:
        u, v = random.choice(G) # picks an edge
        G = merge(G, u, v) # merge subroutine
        vertices = set() 
        for a, b in G:
            vertices.add(a)
            vertices.add(b)
        G = [(a, b) for a, b in G if a != b] # remove self loops

    return len(G) # number of edges left in the edge list is the number of crossing edges remaining

def merge(G, u,v):

    #first stab: basically add everything coming out of node v into the row that denotes edges coming out of node u
    # then go through the whole graph representation and when you come across a link to node v, replace it with node u
    # return the new G

    # basically what i would do is convert all edges coming out of v, into edges coming out of u

    new_edges = []
    for a, b in G:
        a_new = u if a == v else a # that's what's happening here -- everything else is the same
        b_new = u if b == v else b # this does the same thing, everything is the same unless it's going into v, then it goes into u
        new_edges.append((a_new, b_new))
    return new_edges

# this is actually a better implementation because it traverses the edge list once whereas my first stab traverses twice


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 contraction.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    edges = sorted(parse_graph(filepath))
    
    print("First 10 edges:", edges[:10])

    seed = 1234
    cut = contract(edges.copy(), seed)
    print("Cut from one run:", cut)
    
    n = 200
    num_trials = int(n * n * math.log(n))
    best_cut = float('inf')

    for trial_seed in range(num_trials):
        trial_cut = contract(edges.copy(), trial_seed)
        if trial_cut < best_cut:
            best_cut = trial_cut

    print("Best cut found after", num_trials, "trials:", best_cut)

    # print(best_cut)