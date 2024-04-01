#!/usr/bin/python3
"""
Prime Game
"""

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def winner_of_round(n):
    """
    Determine the winner of a round based on the number of primes.
    """
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"

def isWinner(x, nums):
    """
    Determine the overall winner based on the results of multiple rounds.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = winner_of_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
