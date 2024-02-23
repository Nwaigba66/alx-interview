#!/usr/bin/python3
<<<<<<< HEAD
""" prime game
  x: number of rounds
  A: array of n integers
=======
"""This Module defines the isWinner and other helper functions
"""

#!/usr/bin/python3
"""This kodule define the isWinner amd other helper functions
>>>>>>> 361e612cb84af45b9ce5c635a06f59cb2f71c30d
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isWinner(x, nums):
    ben = 0
    maria = 0
    remaining = nums.copy()
    prime = True

    for _ in range(x):
        for _ in range(len(remaining)):
            tempRemaining = list(filter(lambda value: value != 0, remaining))
            if len(tempRemaining) <= 1:
                if ben % 2 == 0:
                    maria += 1
                else:
                    ben += 1
                break
            if ben % 2 == 0:
                while prime:
                  choice = int(input("Marias turn: "))
                  prime = is_prime(choice)
            else:
                while prime:
                  choice = int(input("Bens turn: "))
                  prime = is_prime(choice)

            for i in range(len(remaining)):
                if remaining[i] % choice == 0 and remaining[i] > 1:
                    remaining[i] = 0

        if maria > ben:
            return "Maria"
        else:
            return "Ben"
