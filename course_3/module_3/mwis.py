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

def mwis_membership(path):
    n = len(path) - 1  # path[1..n], 0 is dummy
    A = [0] * (n + 1)   # initialize an array to all zeroes which is the length of the path. we're going to build this array left to right
    A[1] = path[1]

    for i in range(2, n + 1):
        A[i] = max(A[i-1], A[i-2] + path[i])    # in this case path[i] is the weight of the node given in dataset

    # reconstruction
    chosen = set()
    i = n
    while i >= 1:
        if i == 1:
            if A[1] > 0: chosen.add(1) # if you reach 1 then you know you added the first object
            i -= 1
        elif A[i-1] >= A[i-2] + path[i]: # this is the main step: skip if not bigger
            i -= 1
        else:
            chosen.add(i) 
            i -= 2

    return chosen

def mwis_from_file(filename):
        # basically parse weights
    with open(filename) as f:
        n = int(f.readline().strip())
        weights = [0] + [int(line.strip()) for line in f]  # 1-indexed

    chosen = mwis_membership(weights)

    query_vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    bitstring = ''.join('1' if v in chosen else '0' for v in query_vertices) # this is very useful I must learn
    return bitstring

if __name__ == "__main__":
    filename = "mwis.txt"
    print(mwis_from_file(filename))