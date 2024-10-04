import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your longest_path_length function here, along with any subroutines you need
def longest_path_length(n: int, m: int, down: List[List[int]], right: List[List[int]]) -> int:
    """
    Calculate the longest path length in a rectangular grid.
    """
    # Initialize a 2D list to store the longest path lengths
    s = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the first column of the grid
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    # Fill the first row of the grid
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    # Fill the rest of the grid
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]