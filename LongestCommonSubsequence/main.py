import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

sys.setrecursionlimit(10000) # Don't delete! This line is useful to ensure you have sufficient "recursion depth" to store the recursive calls needed for this problem.

# Insert your longest_common_subsequence function here, along with any subroutines you need
def longest_common_subsequence(s: str, t: str) -> str:
    m, n = len(s), len(t)

    # Initialize the length matrix
    length = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the backtrack matrix
    backtrack = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the length and backtrack matrices
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                length[i][j] = length[i-1][j-1] + 1
                backtrack[i][j] = "↖"
            elif length[i-1][j] >= length[i][j-1]:
                length[i][j] = length[i-1][j]
                backtrack[i][j] = "↑"
            else:
                length[i][j] = length[i][j-1]
                backtrack[i][j] = "←"

    # Use OutputLCS to construct the longest common subsequence
    return output_lcs(backtrack, s, m, n)

def output_lcs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "↑":
        return output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "←":
        return output_lcs(backtrack, v, i, j - 1)
    else:
        return output_lcs(backtrack, v, i - 1, j - 1) + v[i-1]

# Test the function
print(longest_common_subsequence("GACT", "ATG"))  # Should print "AT"