import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_kmers function here, along with any subroutines you need
def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Constructs the de Bruijn graph from a collection of k-mers.

    Args:
        patterns: A list of k-mers

    Returns:
        A dictionary representing the De Bruijn graph as an adjacency list
    """
    # Create a dictionary to store the graph
    graph = {}

    # Process each k-mer in the patterns
    for pattern in k_mers:
        # Get prefix and suffix of length k-1
        prefix = pattern[:-1]
        suffix = pattern[1:]

        # Add the prefix to the graph if it's not already there
        if prefix not in graph:
            graph[prefix] = []

        # Add the suffix to the list of neighbors (allowing duplicates)
        graph[prefix].append(suffix)

    # Sort the edges for each node
    for node in graph:
        graph[node].sort()

    return graph

def main():
    # Read input as space-separated k-mers
    patterns = input().strip().split()

    # Get the De Bruijn graph
    result = de_bruijn_kmers(patterns)

    # Print results in the required format
    for node in sorted(result.keys()):
        print(f"{node}: {' '.join(result[node])}")

if __name__ == "__main__":
    main()