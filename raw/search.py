import time

# Our sample data, should be sorted though
dates = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']
prices = [150, 170, 160, 180, 175]

def binary_search(dates, target_date):
    # Initialize the low (left) as 0
    # Initialize the high (right) as the last index
    # len(dates) doesn't start at 0 that's why we have to subtract it by 1
    low, high = 0, len(dates) - 1
    
    # Keep this process on until the low isn't less or equal to high
    while low <= high:
        # Initialize the middle index
        # This divides and gets the remainder of the result
        mid = (low + high) // 2
        
        # Check if it is what we're looking for
        if dates[mid] == target_date:
            return mid  # Return the index where the date is found
          
        # If not, check if it is less than the target
        elif dates[mid] < target_date:
            # We then add the middle index by 1
            # It just searches/moves to the right half of the array
            low = mid + 1
        # If the middle index is not less than the target
        else:
            # So now we search/move to the left half of the array
            high = mid - 1
    return -1  # Return -1 if the date is not found

target_date = '2023-03-01'

start_time = time.perf_counter()
index = binary_search(dates, target_date)
end_time = time.perf_counter()

if index != -1:
    print(f"The stock price on {target_date} was {prices[index]}")
else:
    print(f"Stock price for {target_date} not found")
    
print(f"Search completed in {end_time - start_time:.6f} seconds")

print()

# Our sample data, should be sorted though also
years = [2000, 2005, 2010, 2012, 2015, 2020]
sales = [100, 150, 200, 250, 300, 400]

def interpolation_search(years, target_year):
    # Same initialization for the Binary Search
    low, high = 0, len(years) - 1
    
    # A pretty complex set of condition here
    # We continue if the low is less than or equal to high
    # And we also check if the target is greater or equal to the low value of the array
    # Then vice versa for the last condition
    while low <= high and target_year >= years[low] and target_year <= years[high]:
        # We calculate the position from here on using the interpolation formula
        # This estimates where the target year might be, based on the values at low and high
        pos = low + ((target_year - years[low]) * (high - low)) // (years[high] - years[low])

        # Check if the target year is found at the calculated position pos
        if years[pos] == target_year:
            return pos  # Return the index if the year is found

        # If the target year is greater than the value at pos, move the low boundary up (right)
        elif years[pos] < target_year:
            low = pos + 1
        # If the target year is smaller than the value at pos, move the high boundary down (left)
        else:
            high = pos - 1

        # Return -1 if the year is not found in the list
        return -1

target_year = 2012

start_time = time.perf_counter()
index = interpolation_search(years, target_year)
end_time = time.perf_counter()

if index != -1:
    print(f"Sales in {target_year} were predicted to be {sales[index]}")
else:
    print(f"Sales data for {target_year} not found")
    
print(f"Search completed in {end_time - start_time:.6f} seconds")