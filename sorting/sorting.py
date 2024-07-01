import random
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(list(in_list))

test_cases = [
    {"nums": [4, 2, 6, 3, 4, 6, 2, 1], "output": [1, 2, 2, 3, 4, 4, 6, 6]},
    {"nums": [5, 2, 6, 1, 23, 7, -12, 12, -243, 0], "output": [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]},
    {"nums": [3, 5, 6, 8, 9, 10, 99], "output": [3, 5, 6, 8, 9, 10, 99]},
    {"nums": [99, 10, 9, 8, 6, 5, 3], "output": [3, 5, 6, 8, 9, 10, 99]},
    {"nums": [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0], "output": [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]},
    {"nums": [], "output": []},
    {"nums": [23], "output": [23]},
    {"nums": [42, 42, 42, 42, 42, 42, 42], "output": [42, 42, 42, 42, 42, 42, 42]},
    {"nums": in_list, "output": out_list},
]


def bubble_sort(nums):
    """Bubble sort algorithm that sorts a list of numbers in descending order"""
    # Turn the input (nums) into a list.
    nums = list(nums)

    # Iterate through the input to ensure it is sorted properly
    for _ in range(len(nums) - 1):
        # Iterate through the input, swapping elements of needed
        for i in range(len(nums) - 1):
            # Compare if the currently selected element is greater than the element to the right of it
            if nums[i] > nums[i+1]:
                # Swap the elements if the currently selected element is greater than the element to the right of it
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
    return nums

def bubble_sort_test(start=False):
    """Testing function to test bubble_sort function"""
    if start == True:
        for i, test in enumerate(test_cases):
            fn_output = bubble_sort(test["nums"])
            if fn_output == test["output"]:
                print(f"Test {i + 1}: True")
            else:
                print(f"Test {i + 1}: False - Expected Output: {test['output']}, got {fn_output}")

bubble_sort_test_start = False
bubble_sort_test(bubble_sort_test_start)

def insertion_sort(nums):
    """Performs insertion sort algorithm"""
    # Turn the input into a list 
    nums = list(nums)

    # Iterate through the list starting with the second index/element
    for i in range(1, len(nums)):
        # Initialize the current element
        current = nums[i]
        # Initialize the predecessor index
        j = i-1

        # Shift the sorted list to the right to make space for the current element
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j] # Shift elements to the right
            j -= 1 # Move on to the next element on the left

        # Insert the current element into the correct position. 
        nums[j+1] = current

    # Return the sorted list
    return nums

def insertion_sort_test(start=False):
    """Testing function to test insertion_sort function"""
    if start == True:
        for i, test in enumerate(test_cases):
            fn_output = insertion_sort(test["nums"])
            if fn_output == test["output"]:
                print(f"Test {i + 1}: True")
            else:
                print(f"Test {i + 1}: False - Expected Output: {test['output']}, got {fn_output}")

insertion_sort_test_start = False
insertion_sort_test(insertion_sort_test_start)

def merge(num1, num2):
    """Helper function that merges two sorted lists"""
    # Initialize the resulting list
    result = []
    # Indices for iteration
    i, j = 0, 0
    
    # Loop through the two lists
    while i < len(num1) and j < len(num2):

        # Go through each indice of both list and sort them from least to greatest
        if num1[i] <= num2[j]:
            result.append(num1[i]) # Add the element to the resulting list
            i += 1 # Move on to the next element
        else:
            result.append(num2[j]) # Add the element to the resulting list
            j += 1 # Move on to the next element

    # Append remaining elements from num1 or num2
    result.extend(num1[i:])
    result.extend(num2[j:])

    # Return the result
    return result

def merge_sort(nums):
    """Performs merge sort algorithm"""
    # If the input given is less than or equal to 1 then return it
    if len(nums) <= 1:
        return nums
    
    # Initialize the middle index
    mid = len(nums) // 2

    # Split the input into two halves (left and right)
    left = nums[:mid]
    right= nums[mid:]

    # Recursively sort each half
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Merge the two halves using the merge helper function
    result = merge(left_sorted, right_sorted)

    # Return the result
    return result

def merge_sort_test(start=False):
    """Testing function to test merge_sort function"""
    if start == True:
        for i, test in enumerate(test_cases):
            fn_output = merge_sort(test["nums"])
            if fn_output == test["output"]:
                print(f"Test {i + 1}: True")
            else:
                print(f"Test {i + 1}: False - Expected Output: {test['output']}, got {fn_output}")

merge_sort_test_start = False
merge_sort_test(merge_sort_test_start)


def partition(nums, start=0, end=None):
    """Partitions an array for the quicksort algorithm, returns a selected pivot"""
    # If the end index is not provided, set it to the last index of the array, (note that end is our pivot)
    if end is None:
        end = len(nums) - 1

    # Initialize the left and right pointers
    left, right = start, end - 1

    # Iterate while the left pointer is less than or equal to the right pointer
    while left <= right:
        # If the left pointer is less than or equal to the pivot
        if nums[left] <= nums[end]:
            left += 1 # Increment the left pointer

        # Else if the right pointer is greater than the pivot
        elif nums[right] > nums[end]:
            right -= 1 # Decerement the right pointer

        # Else swap elements if they are out of place
        else:
            nums[left], nums[right] = nums[right], nums[left] # Swap the pairs
            left += 1 # Increment the left pointer
            right -= 1 # Decrement the right pointer 

    # If the left pointer is greater than the pivot
    if nums[left] > nums[end]:
        nums[left], nums[end] = nums[end], nums[left] # Swap the left pointer and the pivot
        return left # Return the left pointer as the new pivot
    
    # Else if the left pointer element is less than or equal to the pivot, the pivot is already in the correct position
    else:
        return end # Return the pivot

def quicksort(nums, start=0, end=None):
    """Performs quicksort algorithm"""
    # If no end index has been provided initialize it
    if end is None:
        nums = list(nums) # Create a copy of the original list
        end = len(nums) - 1 # Initialize the end index

    # Continue the recursion until the start index is less than the end index
    if start < end:
        # Get a pivot index based on the partition helper function
        pivot = partition(nums, start, end)
        # Recursively sort the left half of the array
        quicksort(nums, start, pivot - 1)
        # Recursively sort the right half of the array
        quicksort(nums, pivot + 1, end)

    # Return the result
    return nums

def quicksort_test(start=False):
    """Testing function to test quicksort function"""
    if start == True:
        for i, test in enumerate(test_cases):
            fn_output = quicksort(test["nums"])
            if fn_output == test["output"]:
                print(f"Test {i + 1}: True")
            else:
                print(f"Test {i + 1}: False - Expected Output: {test['output']}, got {fn_output}")

quicksort_test_start = True
quicksort_test(quicksort_test_start)