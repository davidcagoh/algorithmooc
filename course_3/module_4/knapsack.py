# input: knapsack size, number of items, value and size each sbsq row
# output: value of the solution 

# algo idea: 2D array where you iterate on subproblems. go one item at a time, across all sizes (outer loop)

# trick: if we cache more smartly, we'll be able to solve the bigger knapsack problem without issues. 
# cache only as needed and use smart data structures and stuff
# i suspect we have to iterate over all sizes but only some fixed number of items

# notes: 
# anyway add a timer to see how long the code runs
# do the command line heuristic so i can run the code for one file then the bigger :)