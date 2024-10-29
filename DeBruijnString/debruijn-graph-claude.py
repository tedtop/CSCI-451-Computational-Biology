import sys
from typing import List, Dict, Iterable

def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string.
    
    Args:
        text: The input string to process
        k: The length of k-mers to consider
        
    Returns:
        A dictionary representing the De Bruijn graph as an adjacency list
        where keys are (k-1)-mers and values are lists of adjacent (k-1)-mers,
        including duplicates
    """
    # Create a dictionary to store the graph
    graph = {}
    
    # Process each k-mer in the text
    for i in range(len(text) - (k-1)):
        # Get the current (k-1)-mer as the prefix
        kmer = text[i:i+(k-1)]
        # Get the next (k-1)-mer as the suffix
        next_kmer = text[i+1:i+k]
        
        # Add the prefix to the graph if it's not already there
        if kmer not in graph:
            graph[kmer] = []
            
        # Add the suffix to the list of neighbors (allowing duplicates)
        graph[kmer].append(next_kmer)
    
    # Sort the edges for each node
    for node in graph:
        graph[node].sort()
        
    return graph

def main():
    # Read input
    k = int(input().strip())
    text = input().strip()
    
    # Get the De Bruijn graph
    result = de_bruijn_string(text, k)
    
    # Print results in the required format
    for node in sorted(result.keys()):
        print(f"{node}: {' '.join(result[node])}")

if __name__ == "__main__":
    main()
