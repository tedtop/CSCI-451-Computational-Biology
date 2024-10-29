import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_string function here, along with any subroutines you need
def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""

    graph = {}

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        left = kmer[:-1]
        right = kmer[1:]

        if left not in graph:
            graph[left] = []
        if right not in graph[left]:
            graph[left].append(right)

    # Sort the edges for each node
    for node in graph:
        graph[node].sort()

    return graph

def main():
    k = 3
    text = "ACGTGTATA"
    result = de_bruijn_string(text, k)
    for node, edges in result.items():
        print(f"{node}: {' '.join(edges)}")

if __name__ == "__main__":
    main()