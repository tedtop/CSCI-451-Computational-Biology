import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your hamming_distance function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    if len(p) != len(q):
        raise ValueError("Strings must be of equal length.")

    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance