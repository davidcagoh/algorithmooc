# travelling salesman!
# file input: the txt's first line is graph size, then each subsequent line is coordinates of location
# input: complete undirected G(V,E) with V = {1,...,n} and n geq 2
# output: minimum cost of tour of G

## parse file
# get size of graph from first line
# make nxn array for pairwise distances
# for i = (x,y) from 1 to n 
    # for j = (z,w) from i to n
        # do the euclidean distance thing and store in the A[i][j]

## initialize on all choices of subproblems, that's basically all subsets of V with 1 in it, sans 1 with itself
# A = (2^(n-1)-1) * (n-1) 2d array

## base case when tour is of size 2 is basically lengths 
# for j = 2 to n, A[{1,j}][j] = c_1j

## solve with DP
# for s = 3 to n do
    # for S with |S| = s and 1 in S do 
        # for j in S-{1} do
            # A[S][j]= min(over k in S but not 1 or j) (A[S-{j}][k] + c_kj)
# return int(min (over j=2to n) (A[V][j] + c_j1) ## to complete the tour)

import sys, math, time

def read_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        coords = []
        for line in f:
            parts = line.split()
            if len(parts) < 3:
                continue
            x, y = float(parts[1]), float(parts[2])  # skip the vertex label
            coords.append((x, y))
    return n, coords

def euclidean(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.hypot(x1-x2, y1-y2)

def nearest_neighbor(coords):
    n = len(coords)
    visited = [False]*n
    tour = [0]
    visited[0] = True
    total_cost = 0.0
    next_threshold = 10

    for _ in range(n-1):
        last = tour[-1]
        next_city = None
        next_dist = math.inf
        for j in range(n):
            if not visited[j]:
                d = euclidean(coords[last], coords[j])
                if d < next_dist or (abs(d-next_dist) < 1e-9 and (next_city is None or j < next_city)):
                    next_dist = d
                    next_city = j
        tour.append(next_city)
        visited[next_city] = True
        total_cost += next_dist

        percent_done = (len(tour)-1)/n * 100
        if percent_done >= next_threshold:
            print(f"{time.strftime('%H:%M:%S')} - Visited {int(percent_done)}% of cities")
            next_threshold += 10

    # return to start
    total_cost += euclidean(coords[tour[-1]], coords[0])
    return int(total_cost)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tsp_nn.py <inputfile>")
        sys.exit(1)
    n, coords = read_input(sys.argv[1])
    result = nearest_neighbor(coords)
    print(result)