#!/usr/bin/python3
"""
Game of a prime number
"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
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

    Args:
        n (int): The number representing the round.

    Returns:
        str: The winner of the round ("Maria" or "Ben").
    """
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """
    Determine the overall winner of multiple rounds.

    Args:
        x (int): Not used in the function.
        nums (list): A list of numbers representing the rounds.

    Returns:
        str or None: The overall winner ("Maria" or "Ben")
        , or None in case of a tie.
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
