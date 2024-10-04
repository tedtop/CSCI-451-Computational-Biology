import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your reverse_complement function here, along with any subroutines you need
def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    complement_string = ""
    for char in pattern:
        complement_string += get_complement(char)
    return complement_string[::-1]

def get_complement(nucleotide):
    switch = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }
    return switch.get(nucleotide, "Invalid input")

print(reverse_complement("AAAACCCGGT"))