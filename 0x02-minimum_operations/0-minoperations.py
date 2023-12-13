#!/usr/bin/python3
"""This module define a minimum operations
"""
def minOperations(n):
    """An algorithm that check a single character in a text file

    Arguments:
    =========
    file (list of file): represent a single text file

    Returns (interger): True if n is impossible to achieve
    """
    if n == 1:
        return 0

    # Initialize an array to store the minimum operations
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        # Check all possible factors of i
        for j in range(2, i + 1):
            if i % j == 0:
                # Update the minimum operations
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n] if dp[n] != float('inf') else 0
# Example usage
    n = 9
    result = minOperations(n)
    print(f"Number of operations for {n} H characters: {result}")
