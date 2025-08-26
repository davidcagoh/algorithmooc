# basically implement both the mwis computation procedure and the linear backward reconstruction thing
# input: number of nodes and list of weights of each node
# output: a binary code indicating which nodes are in, as you go from left to right

# the pseudocode looks something like:

# initialize an array for the weights
# set S0 = 0, S1 = w1
# from i = 2 to n, S2 = max {(S0 + w2 ), (w1)}
# this should get you the solutions array
# initialize an empty string
# start from the back, if Sn eq Sn-1 then last character of string is 0
# if Sn was MORE than Sn-1 then last character of string is 1
# if Sn is less than Sn-1 throw an error because that shouldn't happen
# iteratively process whole array backward and fill in the string from back to front (append 0 or 1 in front basically)
# return string in proper order :)

# i chose to do this all together instead of modularising because the solutions array should be global enough for the reconstruction to access