#!/usr/bin/python3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def winner_of_round(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
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

