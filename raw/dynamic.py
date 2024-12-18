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
    # The length of the weights
    n = len(weights)
    
    # Initialize a 2d array
    # Loop thru the range of weights added by 1 while we
    # initialize columns with values of zero with the capacity and add 1
    # We add 1 because we need to calculate for the nth index
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Start at index 1 and stop at the last index of weight added by 1
    # This represent the rows
    for i in range(1, n + 1):
        # Then this is for the columns
        # We loop until we reach the capacity added by 1
        for w in range(capacity + 1):
            # In the base, index zero has the value zero from the initialization earlier
            # We compare (if it's less than or equal) 
            # The weight value weights(i - 1) behind the current weight (w)
            if weights[i - 1] <= w:
                # Here we set the result of the max value between the two options
                # Max value is calculate by the previous weight value and
                # The weight value of the previous weight value added by the previous values value
                # A lot of previous here but it's kinda just the concept of
                # Taking a step backward in weights, then taking three steps backward in weights and
                # adding it by another step backward in values
                # Then we set the current row and column to that result of the max
                
                print(dp[i])
                print(weights[i - 1] , "<=" , w)
                print(dp[i - 1][w])
                print(dp[i - 1][w - weights[i - 1]] + values[i - 1])
                print()
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If the current item's weight exceeds the current capacity 
                # We set the the current row and column to the previous row's weight value
                dp[i][w] = dp[i - 1][w]

    # So we then return the value of the nth row (the last index)
    # Which at this point is the max value achievable with all items at full capacity
    return dp[n][capacity]

weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8

start_time = time.perf_counter()
print("\nKnapsack DP Result:", knapsack_dp(weights, values, capacity))  
end_time = time.perf_counter()

print(f"Knapsack DP Execution Time: {end_time - start_time:0.6f} seconds")
