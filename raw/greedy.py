import time

# Helper function :)
def print_dp_array(dp):
    count = 0
    for row in dp:
        print(f"Row {count}: {row}")
        count += 1

def greedy_knapsack(weights, values, capacity):
    # Get the number of items (length of weights array)
    n = len(weights)
    
    # So we have here an array that has the length of our weights
    # For each element in this array, we have a sub-array consisting of
    # For the first column, we go get the values value of the current loop
    # For the second column, we get the weight value of the current loop
    # Then for the last column, we get the value-to-weight ratio for the current loop
    # For the lambda config, we reverse sort (descending) it by referencing index 2 
    items = sorted([(values[i], weights[i], values[i] / weights[i]) for i in range(n)], 
    key=lambda x: x[2], reverse=True)
    
    # Initialize the total value to sum up the values later
    total_value = 0
    
    # Loop thru the items
    for value, weight, ratio in items:
        print_dp_array(items)
        
        print("Total value: ", total_value)
        print("Value: ", value)
        print("Capacity:", capacity)
        print("Weight: ", weight)
        print()
        
        # Check if the remaining capacity can fully accommodate the current item's weight
        # As the loop progresses, the value of capacity and weight is modified
        # Kind of cherry picking through the items
        print(f"{capacity} >= {weight}")
        
        if capacity >= weight:
            # If it is then we subtract capacity from weight
            # This simulates "taking" the item and reducing the available space
            
            print(f"Capacity ({capacity}) - Weight ({weight}) = {capacity - weight}")
            capacity -= weight
            # Then add the total value from the value
            
            print(f"Current item's value {value} will be added to total value")
            total_value += value
        else:  
            # If the capacity is less than the weight
            # We need to account for the available space
            # Doing the same but also multiply it with the ratio of capacity and weight
            # This means we're only taking a fraction of the item
            
            print(f"The ratio of current capacity and current weight is {capacity / weight}")
            print(f"Then multiplied by {value} is {value * (capacity / weight)}\n")
            
            total_value += value * (capacity / weight)
            break
        
        print("Total value after loop: ", total_value)
        print()
    
    return total_value

values = [10, 40, 50, 70]
weights = [1, 3, 4, 5]
capacity = 6

start_time = time.perf_counter()
print("Greedy Knapsack: ", greedy_knapsack(weights, values, capacity)) 
end_time = time.perf_counter()
time_elapsed = end_time - start_time

print(f"Completed in {time_elapsed:.6f} seconds")

print()

def knapsack_divide_and_conquer(weights, values, capacity, n):
    # Base case
    # If no items are left or the knapsack capacity is 0,
    # the total value is 0 (no further items can be added)
    if n == 0 or capacity == 0:
        return 0

    # If the current item's weight does not fit the remaining capacity,
    # skip this item and move to the next one (reduce the problem size by 1 item)
    if weights[n - 1] > capacity:
        return knapsack_divide_and_conquer(weights, values, capacity, n - 1)

    # Option 1
    # Include the current item in the knapsack
    # Add the value of the current item (values[n-1]) to the result of 
    # a recur with reduced capacity (capacity - weights[n-1]) and
    # the remaining items (n-1)
    include = values[n - 1] + knapsack_divide_and_conquer(weights, values, capacity - weights[n - 1], n - 1)

    # Option 2
    # Exclude the current item from the knapsack
    # Recur the same item for the same capacity but now with one less item (n-1)
    exclude = knapsack_divide_and_conquer(weights, values, capacity, n - 1)

    # Pick between the two options for the maximum value
    return max(include, exclude)


weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
n = len(weights)

start_time = time.perf_counter()
print("Divide-and-Conquer Knapsack Result:", knapsack_divide_and_conquer(weights, values, capacity, n))
end_time = time.perf_counter()

time_elapsed = end_time - start_time
print(f"Completed in {time_elapsed:.6f} seconds")
