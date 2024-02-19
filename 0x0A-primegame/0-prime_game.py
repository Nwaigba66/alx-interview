#!/usr/bin/python3
"""This Module defines the isWinner and other helper functions
"""


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(start):
    num = start + 1
    while not is_prime(num):
        num += 1
    return num

def isWinner(x, nums):
    maria_wins = 0
    for n in nums:
        # If n is even, Maria wins directly
        if n % 2 == 0:
            maria_wins += 1
            continue
        # If n is 1, Ben wins directly
        if n == 1:
            continue
        # Starting from 3, each player picks a prime number until no prime number is left
        prime = 3
        while n > 0:
            n -= prime
            prime = next_prime(prime)
        # The player who couldn't pick a prime number loses
        if n == 0:
            maria_wins += 1

    # Determine the winner based on who won the most rounds
    if maria_wins > x // 2:
        return "Maria"
    elif maria_wins < x // 2:
        return "Ben"
    else:
        return None
