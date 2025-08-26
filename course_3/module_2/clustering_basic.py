# basically implement kruskal's global thingy (union find?) and it should be chill
# i think it's even easier than kruskal's algorithm

# input: number of points and a list of pairwise distances: i j cost (basically weighted undirected complete graph)
# output: maximum spacing of a 4-clustering

## outline of code
# parse the data
# initialize number of nodes as number of clusters
# put all the edge weights into a heap (probably a three tuple?) # actually you DON'T need a heap JUST SORT AND GO THRU
# put all nodes in a Union-Find

# extract min the heap and get those nodes
# run Find on UF twice to get cluster names of the nodes 
# if not same cluster, merge those two points together and decrement the total number of clusters
# might need to use union find to ensure that if the nodes are already in the same cluster you skip it 
# once clusters gets to 4, pop the heap and return that distance because that's the spacing

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
    
def parse_graph(filename):
    edges = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for line in f:
            parts = line.strip().split()
            if len(parts) != 3:
                continue
            u, v, cost = int(parts[0]) - 1, int(parts[1]) - 1, int(parts[2])
            edges.append((cost, u, v))
    return edges, n

def max_spacing_k(edges, n, k):
        # Initialize Union-Find structure for clustering
    uf = UnionFind(n)

    # Sort edges by cost in ascending order
    edges.sort(key=lambda x: x[0])

    num_clusters = n

    # Iterate over edges in increasing order of cost
    for cost, u, v in edges:
        # If u and v are in different clusters, union them
        if uf.find(u) != uf.find(v):
            if num_clusters <= k:
                # We have formed k clusters, so the current edge cost is the spacing
                return cost
            uf.union(u, v)
            num_clusters -= 1

    return None  # In case k is larger than number of nodes or no spacing found

if __name__ == "__main__":
    # Example usage: compute max spacing 4-clustering from input file
    input_file = "clustering1.txt"  # Replace with your input filename
    edges, n = parse_graph(input_file)
    k = 4
    spacing = max_spacing_k(edges, n, k)
    print(f"Maximum spacing of {k}-clustering is: {spacing}")
