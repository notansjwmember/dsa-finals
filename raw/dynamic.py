import time

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

# Measure performance for Fibonacci Recursive
start_time = time.perf_counter()
print("\nFibonacci Recursive Result:", fibonacci_recursive(10))
end_time = time.perf_counter()
print(f"Fibonacci Recursive Execution Time: {end_time - start_time:0.6f} seconds")

def knapsack_dp(weights, values, capacity):
    # Get the number of items (length of weights array)
    n = len(weights)
    
    # Create a 2D array to store the max value for each item and capacity combo
    # Rows = items (0 to n), Columns = capacities (0 to capacity)
    # Add 1 to both dimensions to account for the "0-item" and "0-capacity" cases
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Start looping through the items (row by row)
    for i in range(1, n + 1):
        # Now loop through all possible capacities (column by column)
        for w in range(capacity + 1):
            # Check if the current item's weight can fit in the current capacity
            if weights[i - 1] <= w:
                # If the condition is met, we calculate the max value
                # So we've got two options
                # Option 1: Don't include the current item (value from the row above)
                # Option 2: Include the current item:
                #   - Subtract its weight from the current capacity
                #   - Add its value to the result of that remaining capacity (row above)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If it doesn't fit, just carry over the value from the row above (previous item)
                dp[i][w] = dp[i - 1][w]

    # Return the result stored in the bottom-right corner of the table
    # This represents the max value we can get for the given capacity and all items
    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8

start_time = time.perf_counter()
print("\nKnapsack DP Result:", knapsack_dp(weights, values, capacity))  
end_time = time.perf_counter()

print(f"Knapsack DP Execution Time: {end_time - start_time:0.6f} seconds")
