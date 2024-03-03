#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): A list of coin denominations available.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
