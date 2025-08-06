# input: adjacency list representation of G with n = 875000
# output: sizes of 5 largest SCCs in decreasing order

# basic pseudocode
# run DFS-loop subroutine on reversed edges of graph to apply finishing times to every vertex
# run DFS-loop on the graph again but start from the largest finishing times

import sys

def parse_graph(filepath):
    with open(filepath, 'r') as f:
        edges = [int(line.strip()) for line in f if line.strip()]    
    return edges

def DFSLoop(G):
    t = 0 # global variable for finishing times
    s = NULL # global variable for current source vertex / leader vertex
    # should we be initializing an array to track leader vertices here
    # should we be initializing an array to track finishing times here
    # for nodes i = n down to 1
        # if i not explored, set s = i
        # run DFS(G, i)
    return 0

def DFS(G,i):
    # mark i as explored
    # set leader(i) equal to whatever global variable s is
    # for each arc (i,j) in G  
        # if j not explored 
            # DFS (G, j)
    # add 1 to the global value t
    # set f(i) to t
    return 0

# basically starting from node n, you DFS it and label finishing times on the way out. 
# i think after the above is done i would want to check with toy examples if the labelling of finishing times works properly
# later on we have to run DFS loop again on the graph but in the decreasing order of finishing times?
# then after everything we have to add bookkeeping code to keep track of the sizes of all the strongly connected components
# i wonder how to manage the modularity of the code; should i make multiple similar subroutines dealing with reversed edges or something to avoid having to duplicate G?

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 quickSort.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    edges = parse_graph(filepath)
    sizes = main(edges)
    print(sizes)