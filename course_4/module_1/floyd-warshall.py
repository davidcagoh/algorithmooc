# input is directed graph G(V,E) with real weights: The first line indicates the number of vertices and edges, 
# respectively.  Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) 
# and its length (the third number).
# output is dist(v,w) for all v,w in V, or a declaration of "negative cycle"
# idea: index by permissible nodes 1 to k (of course, it's also indexed by choices of v and w)

# function parse graph and initialise base case (file)
# read the txt file which has first line being size of V and E and subsequent lines being source, destination and weight
# A = (nx1) x n x n array
# base case k = 0:
# for v = 1 to n, 
    # for w = 1 to n, 
        # if v = w then A[0][v][w] = 0
        # elif v,w = E then A[0][v][w] = l_vw which is edge weight # actually we can write this AS we're going through the file, no?
        # else A[0][v][w] = plus infinity
# return  the matrix

# fn solve problems (A)
# for k = 1 to n do
    # for v = 1 to n do
        # for w = 1 to n do
            # A[k][v][w] = min ( A[k-1][v][w], A[k-1][v][k] + A[k-1][k][w]) # either inherit or concat two previously available paths
# return the matrix

# fn check cycle and pick smallest pairwise path length (A)
    # check diagonal for any less than 0=, if so print "negative cycle" and terminate
    # else return min {A[n][v][w] for all v,w}


# main script
# for each of g1.txt, g2.txt, g3.txt
    # parse graph 
    # solve with dynamic programming
    # check for negative and pick smallest path length 
# return smallest among them, skipping over any that terminated because of negative cycles detected


import math

def parse_graph(path):
    with open(path, 'r') as f:
        n, m = map(int, f.readline().split())
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for _ in range(m):
            u, v, w = f.readline().split()
            u, v, w = int(u) - 1, int(v) - 1, float(w)
            dist[u][v] = w
    return dist

def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        if dist[i][i] < 0:
            return None
    return dist

def shortest_shortest_path(path):
    dist = parse_graph(path)
    result = floyd_warshall(dist)
    if result is None:
        return None
    min_dist = math.inf
    for i in range(len(dist)):
        for j in range(len(dist)):
            if dist[i][j] < min_dist:
                min_dist = dist[i][j]
    return min_dist, dist

if __name__ == "__main__":
    filenames = ["g1.txt", "g2.txt", "g3.txt"]
    results = []
    for name in filenames:
        res = shortest_shortest_path(name)
        if res is None:
            print(f"Graph {name}: negative cycle")
        else:
            min_dist, dist_matrix = res
            print(f"Graph {name}: shortest shortest path = {min_dist}")
            # for row in dist_matrix:
            #     print(" ".join(f"{x:.2f}" if x != math.inf else "inf" for x in row))
            results.append(min_dist)
    if results:
        print(f"Final answer: {min(results)}")
    else:
        print("Final answer: NULL")
