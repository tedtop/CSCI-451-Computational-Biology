from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        source, dest_weight = edge.split('->')
        dest, weight = dest_weight.split(':')
        source, dest, weight = int(source), int(dest), int(weight)
        graph[source].append((dest, weight))
    return graph

def find_path_to_leaf(graph, start, target, visited, path_length=0):
    if start == target:
        return path_length

    visited.add(start)

    for next_node, weight in graph[start]:
        if next_node not in visited:
            result = find_path_to_leaf(graph, next_node, target, visited, path_length + weight)
            if result is not None:
                return result

    visited.remove(start)
    return None

def solve_leaf_distances(n, edges):
    # Build the graph
    graph = build_graph(edges)

    # Initialize the distance matrix
    distances = [[0] * n for _ in range(n)]

    # Calculate distances between each pair of leaves
    for i in range(n):
        for j in range(i + 1, n):
            # Find distance from leaf i to leaf j
            dist = find_path_to_leaf(graph, i, j, set())
            distances[i][j] = dist
            distances[j][i] = dist  # Matrix is symmetric

    return distances

# Read input from file
with open('dataset_39959_12.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())
edges = [line.strip() for line in lines[1:]]

# Solve and output
result = solve_leaf_distances(n, edges)
for row in result:
    print('\t'.join(str(x) for x in row))