import time

def greedy_knapsack(weights, values, capacity):
    # Get the number of items (length of weights array)
    n = len(weights)
    
    # So we have here an array that has the length of our weights
    # For each element in this array, we have a sub-array consisting of
    # For the first column, we go get the values value of the current loop
    # For the second column, we get the weight value of the current loop
    # Then for the last column, we get the value-to-weight ratio for the current loop
    # For the lambda config, we reverse sort descending) it by referencing index 2 
    items = sorted([(values[i], weights[i], values[i] / weights[i]) for i in range(n)], 
    key=lambda x: x[2], reverse=True)
    
    # Initialize the total value to sum up the values later
    total_value = 0
    
    # Loop thru the items
    for value, weight, ratio in items:
        # print(items)
        # print("Total value: ", total_value)
        # print("Value: ", value)
        # print("Capacity:", capacity)
        # print("Weight: ", weight)
        # print()
        
        # Check if the remaining capacity can fully accommodate the current item's weight
        # As the loop progresses, the value of capacity and weight is modified
        # Kind of cherry picking through the items
        if capacity >= weight:
            # If it is then we subtract capacity from weight
            # This simulates "taking" the item and reducing the available space
            capacity -= weight
            # Then add the total value from the value
            total_value += value
        else:  
            # If the capacity is less than the weight
            # We need to account for the available space
            # Doing the same but also multiply it with the ratio of capacity and weight
            # This means we're only taking a fraction of the item
            
            # print(value * (capacity / weight))
            
            total_value += value * (capacity / weight)
            break

    return total_value

values = [10, 40, 50, 70]
weights = [1, 3, 4, 5]
capacity = 8

start_time = time.perf_counter()
print("Greedy Knapsack: ", greedy_knapsack(weights, values, capacity)) 
end_time = time.perf_counter()
time_elapsed = end_time - start_time

print(f"Completed in {time_elapsed:.6f} seconds")

print()

def knapsack_divide_and_conquer(weights, values, capacity, n):
    # Base conditions
    # If there are no items left or no capacity in the knapsack,
    # the total value is 0.
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the current item exceeds the remaining capacity,
    # we can't include it. Recur by excluding the current item.
    if weights[n - 1] > capacity:
        return knapsack_divide_and_conquer(weights, values, capacity, n - 1)

    # Calculate the value of including the current item:
    # - Add the value of the current item to the result of a recursive call
    #   with reduced capacity and item count.
    include = values[n - 1] + knapsack_divide_and_conquer(weights, values, capacity - weights[n - 1], n - 1)

    # Calculate the value of excluding the current item:
    # - Recur with the same capacity but reduced item count.
    exclude = knapsack_divide_and_conquer(weights, values, capacity, n - 1)

    # Return the maximum value between including and excluding the current item.
    return max(include, exclude)

weights = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
n = len(weights)

start_time = time.perf_counter()
print("Divide-and-Conquer Knapsack: ",knapsack_divide_and_conquer(weights, values, capacity, n))  
end_time = time.perf_counter()

time_elapsed = end_time - start_time

print(f"Completed in {time_elapsed:.6f} seconds")