import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your kmer_composition function here, along with any subroutines you need
def kmer_composition(text: str, k: int) -> Iterable[str]:
    """Forms the k-mer composition of a string."""
    kmers = list()
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return kmers

def main():
    # text = 'CAATCCAAC'
    # k = 5
    # print(kmer_composition(text, k))

    with open(sys.argv[1], 'r') as file:
        k = int(file.readline())
        text = file.readline()

    print(kmer_composition(text, k))

if __name__ == "__main__":
    main()