# input: knapsack size, number of items, value and size each sbsq row
# output: value of the solution 

# algo idea: 2D array where you iterate on subproblems. go one item at a time, across all sizes (outer loop)

# trick: if we cache more smartly, we'll be able to solve the bigger knapsack problem without issues. 
# cache only as needed and use smart data structures and stuff
# i suspect we have to iterate over 2 instead of i rows because you only need the sols from the one-less set of items
# in addition, we have to iterate over at most s_i + 1 columns where s_i is the size of the current object (which is how far back in capacity you need to go to get the subproblem in question)
# more than that, because you use max computations, how about using a max heap? 

# notes: 
# anyway add a timer to see how long the code runs
# do the command line heuristic so i can run the code for one file then the bigger :)

## pseudocode:

# parse the knapsack size C, number of items n, and the items' value and size in each subsequent row

# initialize data structures (array or heap or whatever)
# do the base case, c = 0 to C then set all those to 0 because whenever i = 0 then no items ## or may not be a 2D array but a smarter data structure you know
# for i = 1 to n (inner loop)
# for c = 0 to C (outer loop) do
# if s_i > c then no chance just take the left guy A[i][c] = A[i-1][c]
# else take max { A[i-1][c], A[i-1][c-s_i] + vi} ## but this could be the place where the new data structure comes into play

# return

## bottom line:
# you have 3 lines of code in main: parse, solve, and return. 
# make solve modular? i would ideally want to implement the smart and time/space saving solution right away but i want to do the simple one to sanity check too
# remember we have two files to run, the second is huge but the first one is a doable test to cross check you know. 

import sys, time

sys.setrecursionlimit(10**7)

def parse_input(path):
    with open(path) as f:
        lines = f.read().strip().splitlines()
    capacity, n = map(int, lines[0].split())
    items = [tuple(map(int, line.split())) for line in lines[1:]]
    return capacity, items

def solve_dp(items, capacity):
    start = time.time()
    A = [0] * (capacity + 1)
    for v, w in items:
        for c in range(capacity, w-1, -1):
            A[c] = max(A[c], A[c-w] + v)
    print(f"[DP] finished in {time.time()-start:.2f}s")
    return A[capacity]

def solve_recursive(items, capacity):
    start = time.time()
    n = len(items)
    cache = {}
    def V(i, c):
        if i == 0 or c == 0:
            return 0
        if (i, c) in cache:
            return cache[(i, c)]
        v, w = items[i-1]
        if w > c:
            ans = V(i-1, c)
        else:
            ans = max(V(i-1, c), V(i-1, c-w) + v)
        cache[(i, c)] = ans
        return ans
    result = V(n, capacity)
    print(f"[Recursive] finished in {time.time()-start:.2f}s, cache size={len(cache)}")
    return result

def main(path, mode="dp"):
    capacity, items = parse_input(path)
    if mode == "dp":
        return solve_dp(items, capacity)
    elif mode == "recursive":
        return solve_recursive(items, capacity)
    else:
        raise ValueError("Unknown mode")

if __name__ == "__main__":
    path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "dp"
    print(main(path, mode))