#!/usr/bin/python3
"""This Module defines the isWinner and other helper functions
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    maria_wins = 0
    for n in nums:
        if n == 1 or n % 2 == 0:
            # If n is 1 or even, Ben wins directly
            continue
        maria_wins += 1
    
    # Determine the winner based on who won the most rounds
    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None
