def minOperations(n):
    if n == 1:
        return 0

    # Initialize an array to store the minimum operations needed for each position
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        # Check all possible factors of i
        for j in range(2, i + 1):
            if i % j == 0:
                # Update the minimum operations needed for position i based on previous positions
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage
n = 9
result = minOperations(n)
print(f"Number of operations for {n} H characters: {result}")
