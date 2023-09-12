#!/usr/bin/python3
"""
write a method that calculates the fewest number of operations 
needed to result in exactly n H characters in the file
"""

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize a list to store the minimum operations for each position.
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize the minimum operations for this position to be i.
        dp[i] = i
        for j in range(2, i):
            # If i is divisible by j (j is a factor of i), we can try to copy
            # j characters and then paste (i // j) times to get i characters.
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 + (i // j - 1))

    return db[n]
