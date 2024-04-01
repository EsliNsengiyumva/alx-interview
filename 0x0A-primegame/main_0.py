#!/usr/bin/python3

"""
Script to determine the winner of a prime game.
"""

# Import the isWinner function from the 0-prime_game module
isWinner = __import__('0-prime_game').isWinner

# Print the winner returned by calling isWinner function with arguments 5 and [2, 5, 1, 4, 3]
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
