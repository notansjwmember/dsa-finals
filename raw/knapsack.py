# DP Knapsack
import time

# Helper function :)
def print_dp_array(dp):
    count = 0
    for row in dp:
        print(f"Row {count}: {row}")
        count += 1

def knapsack_dp(weights, values, capacity):
    # Get the number of items (length of weights array)
    n = len(weights)
    print()
    print("Capacity: ", capacity)
    print("Values: ", values)
    print("Weights: ", weights)
    print("Length of weights: ", n)
    print()
    # Create a 2D array to store the max value for each item and capacity combo
    # Rows = items (0 to n), Columns = capacities (0 to capacity)
    # Add 1 to both dimensions to account for the "0-item" and "0-capacity" cases
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    
    # Start looping through the items (row by row)
    # Though we start at row 1, because row 0 is our reference
    for i in range(1, n + 1):
        # Now loop through all possible capacities (column by column)
        # Stop at capacity that is added by 1 to account for the zero base initialization
        
        print("Current dp array: ")
        print_dp_array(dp)
        print()
        
        print(f"Processing row {i}:")

        for w in range(capacity + 1):
            # Check if the current item's weight can fit the current capacity
            # At the base, since i is index 1 then this turns into index 0
            # It lags behind by 1 each loop 
            # W here represents the current column of our dp so at the first it would reference row 0 which is all zero column
            
            print(f"Processing column {w}:")
            print(f"{weights[i-1]} <= {w}")
            
            if weights[i - 1] <= w:
                # If the condition is met, we calculate the max value
                # So we've got two options
                # Option 1: Don't include the current item (value from the row above)
                # Option 2: Include the current item:
                #   - Subtract its weight from the current capacity
                #   - Add its value to the result of that remaining capacity (row above)
                # Option 2 here is basically the previous row's column, added with the value of the current item
                
                print(f"This weight fits the current capacity processed\n")
                print(f"Current row index: {i}")
                print(f"Previous row index: {i-1}")
                print(f"Previous row column value: {dp[i][w]}")
                print(f"Previous row column value subtracted with weight's value: {dp[i][w - weights[i - 1]]}")
                print(f"Then added with the current value: {values[i-1]}")
                option_1 = dp[i-1][w]
                option_2 = dp[i-1][w - weights[i - 1]] + values[i - 1]
                
                print("\nOur options:")
                print("Option 1:", option_1)
                print("Option 2:", option_2)
                
                dp[i][w] = max(option_1, option_2)
                
                print(f"We'll set the this column to {max(option_1, option_2)}")
                
            else:
                # If it doesn't fit, just copy over the value from the row above (previous item)
                dp[i][w] = dp[i - 1][w]
                print(f"This weight does not fit the current capacity processed")
                print(f"This column's value ({dp[i][w]}) will copy {dp[i-1][w]}")
                
            print()
        print()
    
    print("Final dp array: ")
    print_dp_array(dp)
    
    # This represents the max value we can get for the given capacity and all items
    return dp[n][capacity]


weights = [1, 3, 4]
values = [10, 40, 50]
capacity = 6

start_time = time.perf_counter()
print("\nKnapsack DP Result:", knapsack_dp(weights, values, capacity))  
end_time = time.perf_counter()

print(f"Knapsack DP Execution Time: {end_time - start_time:0.6f} seconds")

