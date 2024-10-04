import sys

# Please do not remove package declarations because these are used by the autograder.

"""
MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in first string in Dna
        for each k-mer Pattern' differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns
"""

# Insert your motif_enumeration function here, along with any subroutines you need

# Iterate through all k-mers in the first DNA string, generate their d-neighborhoods, and
# check if each pattern in the neighborhood appears in all DNA strings with at most d mismatches
def motif_enumeration(dna: list[str], k: int, d: int) -> set[str]:
    patterns = set()
    for kmer in get_all_kmers(dna[0], k):
        for pattern in get_d_neighborhood(kmer, d):
            if all(has_approximate_match(seq, pattern, d) for seq in dna):
                patterns.add(pattern)
    return patterns

# Returns all k-mers in a given text
def get_all_kmers(text: str, k: int) -> list[str]:
    return [text[i:i+k] for i in range(len(text) - k + 1)]

# Generate the d-neighborhood of a given pattern
def get_d_neighborhood(pattern: str, d: int) -> list[str]:
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_neighbors = get_d_neighborhood(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.append(nucleotide + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood

# Check if a pattern has an approximate match in a given text with at most d mismatches
def has_approximate_match(text: str, pattern: str, d: int) -> bool:
    return any(hamming_distance(pattern, text[i:i+len(pattern)]) <= d
               for i in range(len(text) - len(pattern) + 1))

def hamming_distance(s1: str, s2: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def parse_file(filename: str):
    with open(filename, 'r') as file:
        # Read the first line and parse k and d
        first_line = file.readline().strip()
        k, d = map(int, first_line.split())

        # Read the second line and split into a list of DNA sequences
        second_line = file.readline().strip()
        dna_sequences = second_line.split()

    return dna_sequences, k, d

def main():
    # Check if filename is provided in argv
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    # Get the filename from command-line arguments
    filename = sys.argv[1]

    # Parse the file and get the dna sequences, k, and d
    dna, k, d = parse_file(filename)

    # Pass the parsed data to the motif_enumeration function
    print(motif_enumeration(dna, k, d))

if __name__ == "__main__":
    main()