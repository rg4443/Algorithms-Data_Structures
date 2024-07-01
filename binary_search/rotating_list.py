# Test Cases for testing functions
test_cases = [
    {"input": [1, 2, 3, 4, 5, 6, 7, 8], "output": 0},
    {"input": [2, 2, 2, 2, 2], "output": 0}, 
    {"input": [1, 1, 1, 1, 1], "output": 0}, 
    {"input": [0, 0, 0, 0, 0], "output": 0},
    {"input": [-1, -1, -1, -1, -1], "output": 0}, 
    {"input": [-5, -5, -5, -5, -5], "output": 0},  
    {"input": [], "output": 0},
    {"input": [1], "output": 0},
    {"input": [8, 1, 2, 3, 4, 5, 6, 7], "output": 1},
    {"input": [2, 1, 2, 2, 2], "output": 1}, 
    {"input": [0, 1, 0, 0, 0], "output": 2},
    {"input": [-3, -3, -5, -5, -5, -4, -3, -3], "output": 2}, 
    {"input": [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], "output": 3},
    {"input": [6, 7, 8, 1, 2, 3, 4, 5], "output": 3},
    {"input": [5, 5, 5, 1, 2, 3, 4, 5], "output": 3}, 
    {"input": [2, 2, 2, 1, 2], "output": 3},
    {"input": [0, 0, 0, 1, 0], "output": 4},
    {"input": [0, 0, 0, 1, 2, 0, 0, 0], "output": 5},  
    {"input": [3, 4, 5, 6, 7, 8, 1, 2], "output": 6},
    {"input": [3, 4, 5, 5, 5, 5, 1, 2], "output": 6},   
    {"input": [-5, -4, -3, -3, -3, -3, -5, -5], "output": 6},  
    {"input": [0, 0, 0, 0, 1, 2, 0, 0], "output": 6}, 
]

def count_rotations_linear(nums):
    """Function that counts the amount of rotations of a given list"""
    # Intilize the length of the input list
    n = len(nums)
    # Iterate through each element in the list
    for element in range(n):
        # Check if the next element is smaller than the current one
        if nums[(element + 1) % n] < nums[element]:
            # Return the remainder of the next element divided by the length of nums
            return (element + 1) % n 
    # Return 0, if no rotations are found
    return 0 

def count_rotations_linear_test(start=False):
    """Function that test count_rotations_linear function via test cases defined on line 2"""
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = count_rotations_linear(test["input"])
            if fn_output == test["output"]:
                print(f"Test {idx+1}: True")
            else:
                print(f"Test {idx+1}: False - Expected Output: {test['output']}, got {fn_output}")

count_rotations_linear_test_start = False
count_rotations_linear_test(count_rotations_linear_test_start)

def count_rotations_binary(nums):
    """Binary Implemenation of counting amount fo rotations in a list"""
    # Intialize the low and high spectrum (indexes) of the array
    low = 0
    high = len(nums) - 1

    # Iterate through the list
    while low <= high:
        # Initialize the mid index
        mid = (low + high) // 2
        # Initialize the middle number of the list
        middle_num = nums[mid]

        # Check if the middle element is the smallest element return it
        if mid > 0 and middle_num < nums[mid - 1]:
            return mid
        
        # Check if mid+1 is the smallest element
        if mid < high and middle_num > nums[mid + 1]:
            return mid + 1
        
        # If the middle number is greater or equal to the first element in the list search the right half
        if middle_num >= nums[low]:
            low = mid + 1
        # Else the middle number is less than the first element so search the left half
        elif middle_num <= nums[low]:
            high = mid - 1

    # Return 0 if the list cannot be rotated if it does not need to be
    return 0

def count_rotations_binary_test(start=False):
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = count_rotations_binary(test["input"])
            if fn_output == test["output"]:
                print(f"Test {idx+1}: True")
            else:
                print(f"Test {idx+1}: False - Expected Output: {test['output']}, got {fn_output}")

count_rotations_binary_test_start = False
count_rotations_binary_test(count_rotations_binary_test_start)

def binary_search(low, high, condition):
    """Binary search function that takes a low and high index as well as the condition function that outputted strings based on which sides should be searched next"""
    # Iterate through the list
    while low <= high:
        # Initialize the middle index
        mid = (low + high) // 2
        # Get the resulting string that the condtion function outputted
        result = condition(mid)

        # If the string is equal to "found", then return it
        if result == "found":
            return result
        # If the string is "left", then search the left half of the list
        elif result == "left":
            high = mid - 1
        # Else (if the string is "right") search the right half of the list
        else:
            low = mid + 1
    
    # Return 0 if not found
    return 0

def count_rotations_generic(nums):
    """Generic implemenation of the counting rotations in a list via using a binary search function and strings to determine which side to search"""
    def condition(mid):
        # Initalize low index of the list
        low = 0
        # Initialize high index of list
        high = len(nums) - 1
        # Initalize middle number
        mid_number = nums[mid]

        # If the middle element is the smallest element return the string "found"
        if mid > 0 and mid_number < nums[mid - 1]:
            return "found"
        # Else if the middle number is less than the last element in the list return the sting "left"
        elif mid_number < nums[high]:
            return "left"
        # Else if the middle number is greater than or equal to the first element in the array return the string "right"
        elif mid_number >= nums[low]:
            return "right"
    
    # Return the output of the binary function by giving it the low and high index, as well as the condition function
    return binary_search(0, len(nums) - 1, condition)

# Testing function for count_rotations_generic
def count_rotations_generic_test(start=False):
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = count_rotations_binary(test["input"])
            if fn_output == test["output"]:
                print(f"Test {idx+1}: True")
            else:
                print(f"Test {idx+1}: False - Expected Output: {test['output']}, got {fn_output}")

count_rotations_generic_test_start = True
count_rotations_generic_test(count_rotations_generic_test_start)