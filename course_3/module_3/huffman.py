# basically code up and run huffman and go, oh, what's the max and min length of encoded character

# input: basically number of nodes and list of relative frequencies
# output: the min and max length in the ultimate tree solution: I guess just traverse 

# pseudo code should be something like 

## parse data
# parse the file by adding all of them to a heap basically
# initialize a heap

## build tree
# initialize tree structure with pointers?
# do extract min twice, get a and b
# make a node point to a (left) and b (right) # merge tree step
# heap-- add a+b
# repeat until done

## traverse tree search
# set i =0, start at root pointer
# every time you travel across a pointer you increment i
# search up character 
# return depth (encoding length)

##main function basically calls the three functions above in sequence, but 
# do traverse tree search twice for lowest and highest frequency character