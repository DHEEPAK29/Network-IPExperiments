import networkx as nx

def calculate_spf(topology_data):
    # topology_data example: [("RouterA", "RouterB", 10), ("RouterB", "RouterC", 20)]
    G = nx.Graph()
    G.add_weighted_edges_from(topology_data)
    
    # Calculate shortest path from 'RouterA' to all nodes
    path_tree = nx.single_source_dijkstra_path(G, "RouterA")
    path_lengths = nx.single_source_dijkstra_path_length(G, "RouterA")
    
    return path_tree, path_lengths

# Example: Link from R1 to R2 (cost 10) and R2 to R3 (cost 5)
topology = [("R1", "R2", 10), ("R2", "R3", 5), ("R1", "R3", 25)]
paths, costs = calculate_spf(topology)
print(f"Shortest path to R3: {paths['R3']} with total cost {costs['R3']}")
