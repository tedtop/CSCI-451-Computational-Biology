import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your overlap_graph function here, along with any subroutines you need
def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""
    overlap_graph = {}
    k = len(patterns[0]) # get length of k-mers in this collection

    # for each k-mer, compare its suffix to the prefix of all other k-mers
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            suffix = patterns[i][1:]
            prefix = patterns[j][:k-1]
            # print(f"compare {patterns[i]} to {patterns[j]}, suffix: {suffix}, prefix: {prefix}")

            if suffix == prefix:

                # if i not in overlap_graph:
                #     overlap_graph[patterns[i]] = patterns[j]
                # else:
                #     overlap_graph[patterns[i]].append(patterns[j])

                overlap_graph.setdefault(patterns[i], set()).add(patterns[j])

    # print(*overlap_graph.items(), sep="\n")
    return overlap_graph

def main():
    input = "AAG AGA ATT CTA CTC GAT TAC TCT TCT TTC"
    patterns = input.split()

    overlap_graph(patterns)


if __name__ == "__main__":
    main()