import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your approximate_pattern_count function here, along with any subroutines you need
def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        pattern_prime = text[i:i+len(pattern)]
        if hamming_distance(pattern, pattern_prime) <= d:
            count += 1
    return count

def hamming_distance(s1: str, s2: str) -> int:
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length.")

    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance