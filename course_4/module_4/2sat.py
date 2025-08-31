# input: a text file with the first line being n, the number of boolean variables from 1 to n. 
# n  also happens to be the number of clauses which will constitute the rest of the input, like "-3 2" means NOT 3 v 2. 
# output: determine which of the 6 files contain satisfiable problems, and encode them in a 6 bit string like 111000. 


## apparently this problem reduced to strongly connected components which you can compute via DFS and kosaraju. you can do
## this by building an implication graph with 2n nodes, with the literals and their negations, and then checking if any
## literal shares an scc with its negation

# adapting my previous kosaraju code:

from collections import defaultdict

# --- 1. Parse 2-SAT file ---
def parse_2sat_file(filepath):
    # First line: number of variables
    # Each subsequent line: two literals for a clause
    clauses = []
    with open(filepath, 'r') as f:
        n = int(f.readline())
        for line in f:
            if line.strip():
                a, b = map(int, line.strip().split())
                clauses.append((a, b))
    return n, clauses

# --- 2. Map literals to unique nodes ---
def var_to_node(x, n):
    # Positive literal x_i -> 1..n
    # Negative literal -x_i -> n+1..2n
    return x if x > 0 else n + (-x)

# --- 3. Build edges from clauses ---
def build_edges(n, clauses):
    edges = []
    for a, b in clauses:
        edges.append((var_to_node(-a, n), var_to_node(b, n)))  # ¬a -> b
        edges.append((var_to_node(-b, n), var_to_node(a, n)))  # ¬b -> a
    return edges

# --- 4. Build graph and reversed graph ---
def build_graph(edges, num_nodes):
    G, G_rev = defaultdict(list), defaultdict(list)
    for u, v in edges:
        G[u].append(v)
        G_rev[v].append(u)
    # Ensure all nodes exist even if no outgoing edges
    for i in range(1, num_nodes+1):
        G[i]; G_rev[i]
    return G, G_rev

# --- 5. Kosaraju SCC ---
def kosaraju_scc(edges, num_nodes):
    G, G_rev = build_graph(edges, num_nodes)
    
    # --- First pass: compute finishing times on reversed graph ---
    explored, finishing_order = set(), []
    def dfs_first(node):
        stack = [node]
        visited = set()
        while stack:
            v = stack[-1]
            if v not in explored:
                explored.add(v)
                visited.add(v)
                for nei in G_rev[v]:
                    if nei not in explored:
                        stack.append(nei)
            else:
                stack.pop()
                if v in visited:
                    finishing_order.append(v)
                    visited.remove(v)
    
    for node in range(1, num_nodes+1):
        if node not in explored:
            dfs_first(node)

    # --- Second pass: find SCCs in original graph ---
    explored.clear()
    sccs = []
    def dfs_second(node, scc):
        stack = [node]
        while stack:
            v = stack.pop()
            if v not in explored:
                explored.add(v)
                scc.append(v)
                for nei in G[v]:
                    if nei not in explored:
                        stack.append(nei)
    
    for node in reversed(finishing_order):
        if node not in explored:
            scc = []
            dfs_second(node, scc)
            sccs.append(scc)
    
    return sccs

# --- 6. Check satisfiability ---
def is_satisfiable(sccs, n):
    """
    Determines if the 2-SAT instance is satisfiable by checking SCCs.
    Args:
        sccs: list of SCCs, each SCC is a list of node indices
        n: number of boolean variables
    Returns:
        True if satisfiable, False if unsatisfiable
    """
    # Map each node to the index of its SCC
    node_to_scc = {}
    for i, scc in enumerate(sccs):
        for node in scc:
            node_to_scc[node] = i
    
    # For each variable x_i, check if x_i and -x_i are in the same SCC
    for i in range(1, n+1):
        # Positive literal node: i
        # Negative literal node: i + n
        if node_to_scc[i] == node_to_scc[i+n]:
            # If they are in the same SCC, the formula is unsatisfiable
            # Because a path exists both ways between x_i and ¬x_i
            return False
    
    # No conflicts found, the formula is satisfiable
    return True

# --- Example usage ---
if __name__ == "__main__":
    result_bits = []
    for i in range(1, 7):
        filename = f'2sat{i}.txt'
        n, clauses = parse_2sat_file(filename)
        edges = build_edges(n, clauses)
        num_nodes = 2 * n
        sccs = kosaraju_scc(edges, num_nodes)
        sat = is_satisfiable(sccs, n)
        print(f"{filename} Satisfiable? {sat}")
        result_bits.append('1' if sat else '0')
    binary_result = ''.join(result_bits)
    print("Binary string of satisfiable files:", binary_result)

