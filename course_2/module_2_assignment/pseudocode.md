okay let's figure out how to make this

# input: a giant txt file with each line corresponding to a vertex, and each line has the directed links comma weights
# output: report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197.

so we only need to run djikstra about 10 times. 

# main
- parser
- run main 

djikstra initializes with a single node and distance 0. then you go through all the node's neighbours and expand the frontier. you go through the neighbours of X, and sort and stuff.

djikstra(start, target)
- make a set visited with just start
- make an array Dist of length = n full of positive infinity, and Dist(start) set to 0
while X does not include 7,37,59,82,99,115,133,165,188,197, do main loop
- return Dist(7),Dist(37)... in order. 


def traverse which is main loop ! 
go through all v in visited and check if there exists edge (v,w) with v in visited and w not in visited
if empty, break
if not empty,
initialize heap
for each edge, compute Dist(v) + value of edge(v,w)  and insert to heap
extractmin from heap to get edge V*, w*
add w* to set X
set Dist(w*) to Dist(v*) + value of edge(v,w)

# In the focused heap implementation, after you explore w you add all its neighbours to your frontier heap and keep going