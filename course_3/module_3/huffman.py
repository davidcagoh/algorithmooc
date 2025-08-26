# basically code up and run huffman and go, oh, what's the max and min length of encoded character

# input: basically number of nodes and list of relative frequencies
# output: the min and max length in the ultimate tree solution: I guess just traverse 

# pseudo code should be something like 

## parse data
# initialize a heap
# parse the file by adding all of them to a heap basically

## build tree
# initialize tree structure with pointers? basically i think we need to start with all the nodes separate and merge as we go along
# do extract min on heap twice, get a and b
# in tree, make a node point to a (left) and b (right) # merge tree step
# heap-- add a+b
# repeat until done

## traverse tree search
# set i =0, start at root pointer
# every time you travel across a pointer you increment i
# search up character 
# return depth (encoding length)

##main function basically calls the three functions above in sequence, but 
# do traverse tree search twice for lowest and highest frequency character

import heapq

def huffman_code_lengths_from_file(path):
    # parse the weights
    with open(path) as f:
        n = int(f.readline().strip())        # number of symbols
        weights = [int(line.strip()) for line in f]

    #initialize the heap
    # Each heap element is a tuple: (weight, min_depth, max_depth).
    # Leaf nodes start with depth = 0 (since no edges yet).
    heap = [(w, 0, 0) for w in weights]
    heapq.heapify(heap)

    # do the tree buiding process
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        # Merge two nodes: weight adds up.
        # Depth increases by 1 for all leaves under this new node.
        new_weight = a[0] + b[0]
        new_min = min(a[1], b[1]) + 1
        new_max = max(a[2], b[2]) + 1
        heapq.heappush(heap, (new_weight, new_min, new_max))

    _, min_len, max_len = heap[0]
    return min_len, max_len

# Example run
import sys 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python huffman.py <inputfile>")
        sys.exit(1)
    infile = sys.argv[1]
    min_len, max_len = huffman_code_lengths_from_file(infile)
    print("Minimum codeword length:", min_len)
    print("Maximum codeword length:", max_len)