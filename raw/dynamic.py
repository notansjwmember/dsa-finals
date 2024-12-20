import time
import os

os.system('cls')
def fibonacci_dp(n):
    # Base conditions
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Initialize an array of zeroes with the length of the n and add 1
    # Why add 1? Because we need to reference the first index
    dp = [0] * (n + 1)
    
    # Set the first and second index as 0,1 (fixed for fibo)
    dp[0], dp[1] = 0, 1
    
    # Start at index 3, since we've come across the indices 1 and 2
    # We complement the stop by adding 1 since earlier we added 1 for the initial array
    for i in range(2, n + 1):
        # For the current index in the loop
        # We calculate the previous index value and the previous previous index of the value
        # Like one step back then two steps back
        # So like you know just add it
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # After the loop, we return the result
    return dp[n]

start_time = time.perf_counter()
print("Fibonacci DP Result:", fibonacci_dp(10))
end_time = time.perf_counter()
print(f"Fibonacci DP Execution Time: {end_time - start_time:0.6f} seconds")

def fibonacci_recursive(n):
    # Base conditions
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # For any other value of n, calculate the Fibonacci number by calling the function recursively
    # This calls this method for (n-1) and (n-2), summing their results
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

start_time = time.perf_counter()
print("\nFibonacci Recursive Result:", fibonacci_recursive(8))
end_time = time.perf_counter()
print(f"Fibonacci Recursive Execution Time: {end_time - start_time:0.6f} seconds")
