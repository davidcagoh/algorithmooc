import heapq

def parse_graph(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
            v = int(parts[0])
            edges = []
            for token in parts[1:]:
                nbr, w = token.split(',')
                edges.append((int(nbr), int(w)))
            graph[v] = edges
    return graph

def dijkstra(graph, start, targets):
    visited = set([start])
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    heap = []

    while not all(t in visited for t in targets):
        for v in visited:
            for w, weight in graph[v]:
                if w not in visited:
                    heapq.heappush(heap, (dist[v] + weight, v, w))
        while heap:
            d, v_star, w_star = heapq.heappop(heap)
            if w_star not in visited: # not sure if this one is necessary
                visited.add(w_star)
                dist[w_star] = d
                break
        else:
            break
    return [dist[t] for t in targets]

if __name__ == "__main__":
    filename = "input.txt"
    graph = parse_graph(filename)
    targets = [7,37,59,82,99,115,133,165,188,197]
    distances = dijkstra(graph, 1, targets)
    print(",".join(str(d) for d in distances))
   
   # possible modifications include sanity check for the targets being actually reachable
   # setting the 10 million value for unable to reach
   # two round knockout tournament to frontload all the frontier edge calculations