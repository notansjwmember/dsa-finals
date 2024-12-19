import random
import time
from datetime import datetime, timedelta

# Generate mock filenames without worrying about their file sizes
# This speeds up lookups as we don't need to fetch or wait for the actual file data
def generate_filenames(n):
    return [f"file_{i}.txt" for i in range(1, n+1)]

# Generate a list of random numbers
# The number of random numbers is determined by the n parameter
# While the start and end parameters define the range (default: 1 to 1000)
# The n value varies based on the provided configuration
def generate_random_numbers(n, start=1, end=1000):
    return [random.randint(start, end) for _ in range(n)]

# Generate a list of random dates
def generate_random_dates(n):
    # Base date (January 1, 2020)
    start_date = datetime(2020, 1, 1)
    
    # From the base, we add a random generated day
    # For example, if the random is 5 then we add 5 days to the base date
    # So in here we randomized from 0 to 1000 days to add
    # Don't forget that this is an array, so we loop until we reach the n parameter
    return [start_date + timedelta(days=random.randint(0, 1000)) for _ in range(n)]

def selection_sort(arr):
    n = len(arr) # Get the size of array
    
    for i in range(n): 
        # At the start we initialize the minimum index which at first would be the first index
        # Then as it loops, it will be modified to the least of the least index in the array
        min_idx = i
        
        # j in here represents the next index of i
        # The loop's start is incremented by 1
        # Basically decreasing the elements of the array in each loop
        # For example, we were given a n of 5
        # That would be like, 1-2-3-4-5
        # Doesn't sound like much but it means that in every loop
        # we start at the next index so in result the elements decreases
        for j in range(i+1, n):
            # At the base we check if the j here in this current loop is less than the minimum index
            # But as the loop goes on the minimum index also changes (if the condition was met)
            if arr[j] < arr[min_idx]:
                # If the condition was met then modify the minimum index
                # The j in here will now be the new minimum index
                min_idx = j
        # After the second loop, in this first loop we then swap
        # Swapping here takes the initial index then the winner of the second loop (the min index)
        # To where the initial index was before
        # Thus we call it "selection" sort, cuz we select what we need to swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    # If the array has one or zero elements, it's already sorted, so return it as is
    if len(arr) <= 1:
        return arr
    
    # Our reference to compare the right and left side of the array
    # Essentially it is the element that is in the middle of the (current) array
    pivot = arr[len(arr) // 2]
    
    # Left side of the array (or the lesser elements of the current pivot)
    # We add the elements that meet the condition (if the element is less than the reference)
    left = [x for x in arr if x < pivot]
    
    # We just get the middle element from here
    middle = [x for x in arr if x == pivot]
    
    # Right side of the array (or the greater elements of the current pivot)
    # Same logic for the left side of the array but now 
    # the condition is if the element is greater than reference
    right = [x for x in arr if x > pivot]
    
    # Recursively do method to the left and right sub-arrays,
    # and concatenate the results: left + middle + right
    return quick_sort(left) + middle + quick_sort(right)

small_dataset_size = 10
large_dataset_size = 1000

small_files = generate_filenames(small_dataset_size)
large_files = generate_filenames(large_dataset_size)

small_numbers = generate_random_numbers(small_dataset_size)
large_numbers = generate_random_numbers(large_dataset_size)

small_dates = generate_random_dates(small_dataset_size)
large_dates = generate_random_dates(large_dataset_size)


# Data to process
print("Processing mock files..\n")

# Size of data to process
print("Small data:")

# For selection sort
start_time = time.perf_counter()
sorted_small_files_selection = selection_sort(small_files.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Small Files: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_small_files_quick = quick_sort(small_files.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Small Files: Time elapsed: {end_time - start_time:.6f} seconds")
print()

# Size of data to process
print("Large data:")

# For selection sort
start_time = time.perf_counter()
sorted_large_files_selection = selection_sort(large_files.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Large Files: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_large_files_quick = quick_sort(large_files.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Large Files: Time elapsed: {end_time - start_time:.6f} seconds")
print()

# Data to process
print("Processing random numbers..\n")

# Size of data to process
print("Small data:")

# For selection sort
start_time = time.perf_counter()
sorted_small_numbers_selection = selection_sort(small_numbers.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Small Numbers: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_small_numbers_quick = quick_sort(small_numbers.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Small Numbers: Time elapsed: {end_time - start_time:.6f} seconds")
print()

# Size of data to process
print("Large data:")

# For selection sort
start_time = time.perf_counter()
sorted_large_numbers_selection = selection_sort(large_numbers.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Large Numbers: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_large_numbers_quick = quick_sort(large_numbers.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Large Numbers: Time elapsed: {end_time - start_time:.6f} seconds")
print()

# Data to process
print("Processing random dates..\n")

# Size of data to process
print("Small data:")

# For selection sort
start_time = time.perf_counter()
sorted_small_dates_selection = selection_sort(small_dates.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Small Dates: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_small_dates_quick = quick_sort(small_dates.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Small Dates: Time elapsed: {end_time - start_time:.6f} seconds")
print()

# Size of data to process
print("Large data:")

# For selection
start_time = time.perf_counter()
sorted_large_dates_selection = selection_sort(large_dates.copy())
end_time = time.perf_counter()
print(f"Selection Sort - Large Dates: Time elapsed: {end_time - start_time:.6f} seconds")

# For quick sort
start_time = time.perf_counter()
sorted_large_dates_quick = quick_sort(large_dates.copy())
end_time = time.perf_counter()
print(f"Quick Sort - Large Dates: Time elapsed: {end_time - start_time:.6f} seconds")
