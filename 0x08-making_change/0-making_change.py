#!/usr/bin/python3

def makeChange(coins, total):
    if total < 0:
        return -1
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for t in range(1, total + 1):
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], dp[t - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    total = 30
    print(makeChange(coins, total))

