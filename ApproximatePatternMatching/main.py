import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_matching function here, along with any subroutines you need
def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
            positions.append(i)
    return positions

def hamming_distance(p: str, q: str) -> int:
    if len(p) != len(q):
        raise ValueError("Strings must be of equal length.")

    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance
