# i have no idea how to do this hamming distance one

# input: a whole lot of nodes represented as a list of 24 bit labels representing their position (distance is number of different bits)
# output: number of unique clusters if the spacing is at least 3

## conceptual pseudocode

# nodes = {convert each bit-string to int: node_id}
# store in a hashtable or something 
# uf = UnionFind(number_of_nodes)

# for each node x in nodes:
#       use bitwise operations to find all nodes with difference just 1 = 1_neighbours
#       use bitwise operations to find all nodes with difference just 2 = 2_neighbours
#     neighbors = all nodes at Hamming distance 1 or 2 = 1_nei + 2_nei
#     for neighbor in neighbors:
#         if neighbor in nodes:
#             uf.union(x, neighbor)

# return number of unique clusters = len(set(uf.find(x) for x in nodes))

## Union Find from last time (implemented)

class UnionFind:
    def __init__(self, n):
        # Initialize parent and rank arrays for Union-Find
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        # Path compression heuristic
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        # Union by rank heuristic
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False  # Already in the same set
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
        return True
    

def parse_nodes(filename):
    """
    Parse the input file to extract node bit labels as integers.
    The first line contains two integers: number of nodes and number of bits.
    Each subsequent line contains a bit label with bits separated by spaces.
    Returns a list of integers representing the nodes.
    """
    nodes = []
    with open(filename, 'r') as f:
        first_line = f.readline()
        num_nodes, num_bits = map(int, first_line.split())
        for _ in range(num_nodes):
            bits = f.readline().strip().split()
            # Convert bit list to integer
            node_int = 0
            for bit in bits:
                node_int = (node_int << 1) | int(bit) # the left shift makes space for the bit: a 0 on the right side basically
            nodes.append(node_int)
    return nodes


## main code
def letsgo(nodes):
    # read nodes as integers
    nodes_set = set(nodes)
    nodes = list(set(nodes))    # Create a mapping from node integer to its index for O(1) lookups
    node_to_index = {node: idx for idx, node in enumerate(nodes)}
    uf = UnionFind(len(nodes))
 
    for idx,node in enumerate(nodes):
        # Hamming distance 1 neighbors
        for i in range(24): # for 24 possible one bit flips
            n1 = node ^ (1<<i) ## generate  possible neighbor by fliping that bit
            if n1 in nodes_set: # check if neighbours actually exist
                # Use the mapping for O(1) index lookup instead of nodes.index()
                uf.union(idx, node_to_index[n1]) # merge if they are


        # Hamming distance 2 neighbors # same here
        for i in range(24):
            for j in range(i+1,24): # but now we allow ourselves to flip two bits 
                n2 = node ^ (1<<i) ^ (1<<j)
                if n2 in nodes_set:
                    # Use the mapping for O(1) index lookup instead of nodes.index()
                    uf.union(idx, node_to_index[n2])

    # number of clusters
    clusters = len(set(uf.find(i) for i in range(len(nodes))))
    return clusters

if __name__ == "__main__":
    # Example usage: compute max spacing 4-clustering from input file
    input_file = "clustering_big.txt"  # Replace with your input filename
    nodes = parse_nodes(input_file)
    clusters = letsgo(nodes)
    print(f"Number of clusters that are 3 or more distance away is: {clusters}")


## basically my error at first was using that dictionary thing. 
# i did not turn it back to list(set(nodes)) ppst deduplicate which caused some double counting