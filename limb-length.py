def limb_length(n, j, D):
    """
    Calculate the limb length for leaf j in a phylogenetic tree
    
    Parameters:
    n (int): Number of leaves in the tree
    j (int): Index of the leaf whose limb length we want to calculate (0-based)
    D (list): n x n distance matrix
    
    Returns:
    int: The limb length for leaf j
    """
    # Initialize minimum length to a large value
    min_length = float('inf')
    
    # Iterate through all pairs of leaves i,k where i≠j and k≠j
    for i in range(n):
        if i != j:
            for k in range(i + 1, n):
                if k != j:
                    # Calculate (Di,j + Dj,k - Di,k)/2
                    length = (D[i][j] + D[j][k] - D[i][k]) // 2
                    min_length = min(min_length, length)
    
    return min_length

# Read input
def parse_input():
    n = int(input())
    j = int(input())
    D = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        D.append(row)
    return n, j, D

# Main execution
if __name__ == "__main__":
    n, j, D = parse_input()
    result = limb_length(n, j, D)
    print(result)
