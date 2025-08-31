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

import sys, math

def read_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        coords = [tuple(map(float, line.split())) for line in f]
    return n, coords

def build_dist_matrix(coords):
    n = len(coords)
    dist = [[0.0]*n for _ in range(n)]
    for i in range(n):
        x1,y1 = coords[i]
        for j in range(n):
            x2,y2 = coords[j]
            dist[i][j] = math.hypot(x1-x2, y1-y2)
    return dist

def held_karp(dist):
    n = len(dist)
    dp = [[math.inf]*n for _ in range(1<<n)]
    # base cases
    for j in range(1,n):
        dp[(1<<0)|(1<<j)][j] = dist[0][j]
    # fill DP
    for mask in range(1<<n):
        if not (mask & 1): continue  # must contain city 0
        for j in range(1,n):
            if not (mask & (1<<j)): continue
            prev_mask = mask ^ (1<<j)
            for k in range(1,n):
                if (prev_mask & (1<<k)):
                    dp[mask][j] = min(dp[mask][j], dp[prev_mask][k] + dist[k][j])
    # final answer
    full_mask = (1<<n)-1
    ans = min(dp[full_mask][j] + dist[j][0] for j in range(1,n))
    return int(ans)  # round down

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tsp.py <inputfile>")
        sys.exit(1)
    n, coords = read_input(sys.argv[1])
    dist = build_dist_matrix(coords)
    result = held_karp(dist)
    print(result)