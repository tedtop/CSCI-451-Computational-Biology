import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

from typing import List

# Insert your change function here, along with any subroutines you need
def change(money: int, coins: List[int]) -> int:
    """
    Function solving the Change Problem.
    """
    # Initialize a list to store the minimum number of coins needed for each amount of money
    min_coins = [float('inf')] * (money + 1)
    min_coins[0] = 0  # Base case: 0 coins are needed to make 0 money

    # Iterate over each coin
    for coin in coins:
        for m in range(coin, money + 1):
            if min_coins[m - coin] + 1 < min_coins[m]:
                min_coins[m] = min_coins[m - coin] + 1

    # If no solution is found, return -1
    return min_coins[money] if min_coins[money] != float('inf') else -1