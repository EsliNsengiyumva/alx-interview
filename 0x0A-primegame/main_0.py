#!/usr/bin/python3

import_name = __import__('0-prime_game')
is_winner = import_name.isWinner

print("Winner: {}".format(is_winner(5, [2, 5, 1, 4, 3])))
