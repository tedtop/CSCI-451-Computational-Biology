from collections import defaultdict

def parse_input():
    n = int(input())
    D = []
    for _ in range(n):
        row = list(map(float, input().split()))
        D.append(row)
    return D, n

def find_closest_clusters(D, clusters):
    min_dist = float('inf')
    min_i = min_j = 0
    n = len(D)
    
    for i in range(n):
        for j in range(i + 1, n):
            if D[i][j] < min_dist:
                min_dist = D[i][j]
                min_i = i
                min_j = j
    
    # Get actual cluster indices from the current clusters list
    ci = clusters[min_i]
    cj = clusters[min_j]
    return ci, cj, min_dist

def compute_new_distances(D, ci_idx, cj_idx, ci_size, cj_size):
    n = len(D)
    new_distances = []
    
    # Calculate distances to the new cluster for all other clusters
    for k in range(n):
        if k != ci_idx and k != cj_idx:
            # UPGMA formula: weighted average of distances
            new_dist = (ci_size * D[k][ci_idx] + cj_size * D[k][cj_idx]) / (ci_size + cj_size)
            new_distances.append(new_dist)
    
    return new_distances

def update_distance_matrix(D, ci_idx, cj_idx, new_distances):
    n = len(D)
    new_D = []
    new_dist_idx = 0
    
    # Create new matrix excluding ci_idx and cj_idx rows/columns
    for i in range(n):
        if i != ci_idx and i != cj_idx:
            row = []
            for j in range(n):
                if j != ci_idx and j != cj_idx:
                    row.append(D[i][j])
            # Add distance to new cluster
            row.append(new_distances[new_dist_idx])
            new_D.append(row)
            new_dist_idx += 1
    
    # Add row for new cluster
    new_D.append(new_distances + [0])
    
    return new_D

def UPGMA(D, n):
    # Initialize clusters and tree
    clusters = list(range(n))  # Initial cluster labels
    cluster_sizes = defaultdict(lambda: 1)  # Track size of each cluster
    tree = defaultdict(list)  # Adjacency list representation
    age = defaultdict(float)  # Age (height) of each node
    next_node = n  # Label for next internal node
    
    while len(clusters) > 1:
        # Find closest clusters
        ci, cj, dist = find_closest_clusters(D, clusters)
        
        # Create new cluster
        new_cluster = next_node
        next_node += 1
        
        # Calculate age of new node
        age[new_cluster] = dist / 2
        
        # Add edges to tree (both directions)
        # Edge length = parent age - child age
        edge_to_ci = age[new_cluster] - age[ci]
        edge_to_cj = age[new_cluster] - age[cj]
        
        tree[new_cluster].append((ci, edge_to_ci))
        tree[ci].append((new_cluster, edge_to_ci))
        tree[new_cluster].append((cj, edge_to_cj))
        tree[cj].append((new_cluster, edge_to_cj))
        
        # Update clusters
        ci_idx = clusters.index(ci)
        cj_idx = clusters.index(cj)
        
        # Calculate new distances
        new_distances = compute_new_distances(
            D, ci_idx, cj_idx,
            cluster_sizes[ci],
            cluster_sizes[cj]
        )
        
        # Update distance matrix
        D = update_distance_matrix(D, ci_idx, cj_idx, new_distances)
        
        # Update cluster information
        clusters.remove(ci)
        clusters.remove(cj)
        clusters.append(new_cluster)
        
        # Update cluster size
        cluster_sizes[new_cluster] = cluster_sizes[ci] + cluster_sizes[cj]
    
    return tree

def print_tree(tree):
    # Print adjacency list with formatted edge weights
    for node in sorted(tree.keys()):
        for neighbor, weight in sorted(tree[node]):
            print(f"{node}->{neighbor}:{weight:.3f}")

def main():
    D, n = parse_input()
    tree = UPGMA(D, n)
    print_tree(tree)

if __name__ == "__main__":
    main()
