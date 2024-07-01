# Longest common subsequence test cases
lcq_test_cases = [
    {"str1": "serendipitous", "str2": "precipitation", "output": 7},
    {"str1": [1, 3, 5, 6, 7, 2, 5, 2, 3], "str2": [6, 2, 4, 7, 1, 5, 6, 2, 3], "output": 5},
    {"str1": "longest", "str2": "stone", "output": 3},
    {"str1": "asdfwevad", "str2": "opkpoiklklj", "output": 0},
    {"str1": "dense", "str2": "condensed", "output": 5},
    {"str1": "", "str2": "opkpoiklklj", "output": 0},
    {"str1": "", "str2": "", "output": 0},
    {"str1": "abcdef", "str2": "badcfe", "output": 3},
]

# LCQ SOLUTIONS & LCQ TESTS
def lcq_recursive(str1, str2, idx1=0, idx2=0):
    """Algorithm that determines the longest common subsequence in two strings"""
    # Check if we have reached the end of either subsequence
    if idx1 == len(str1) or idx2 == len(str2):
        return 0  
    # Check if the current characters being compared are equal if so then recursively return 1 along with moving on to the next char
    if str1[idx1] == str2[idx2]:
        return 1 + lcq_recursive(str1, str2, idx1+1, idx2+1)
    # If the chars do not match then find the LCS either by skipping the current char of the first string or skipping the current char
    # of the second string, depending on which ever string is the longest per iteration
    else:
        return max(lcq_recursive(str1, str2, idx1+1, idx2), lcq_recursive(str1, str2, idx1, idx2+1))

def lcq_recursive_test(start=False):
    """Test lcq_recursive function via iterating through test cases and examining its outputs compared it to the expected output"""
    if start == True:
        for idx, test in enumerate(lcq_test_cases):
            fn_output = lcq_recursive(test["str1"], test["str2"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

lcq_recursive_test_start = False
lcq_recursive_test(lcq_recursive_test_start)

def lcq_memoized(str1, str2):
    """More optimized apporach of implementing Longest Common Subsequnce algorithm using memoization"""
    # Initialize a dict for memoization that resuses results
    memo = {}

    def recurse(idx1, idx2):
        """Performs the Longest Common Subsequence Algorithm via use of recursion"""
        # Create a key for the current indices
        key = idx1, idx2
        # If the result is already computed, then reuse it via memoization and return it
        if key in memo:
            return memo[key]
        # If we have reached the end of either string, have the length of the LCS be 0 meaning that there are no more
        # chars to compare
        if idx1 == len(str1) or idx2 == len(str2):
            memo[key] = 0
        # If the chars that are being compared are equal add it to the LCS and move on
        elif str1[idx1] == str2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        # If the two chars that are being compared are not equal, then have two choices: swap the char in the first string, or the 
        # char in the second string, whichever string has the most elements/values.
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        # Return the final string
        return memo[key]
    
    # Start the recursion but with the initial indices being 0, 0.
    return(recurse(0,0))

def lcq_memoized_test(start=False):
    """Test lcq_memoized function via iterating through test cases and examining its outputs compared to the expected output"""
    if start == True:
        for idx, test in enumerate(lcq_test_cases):
            fn_output = lcq_memoized(test["str1"], test["str2"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

lcq_memoized_test_start = False
lcq_memoized_test(lcq_memoized_test_start)

def lcq_dp(str1, str2):
    """Implements Longest Common Subsequence Algorithm via dynamic programming of creating a table of (n1+1) by (n2+1)"""
    # Initialize the length of both strings
    n1, n2 = len(str1), len(str2)
    # Create a table of dimensions (n1+1) by (n2+1) populating all elements with zeros 
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    # Iterate through the first string
    for idx1 in range(n1):
        # Iterate through the second string
        for idx2 in range(n2):
            # If the chars being compared match
            if str1[idx1] == str2[idx2]:
                # Increment the cell diagonally to the right by 1, indicating a match
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            # If chars don't match then take the max value of the cell above or to the left to determine which char is swapped
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])

    # Return the length of the longest common subsequence for the two string
    return results[-1][-1]

def lcq_dp_test(start=False):
    """Test lcq_dp function via iterating through test cases and examining its outputs compared to the expected output"""
    if start == True:
        for idx, test in enumerate(lcq_test_cases):
            fn_output = lcq_dp(test["str1"], test["str2"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

lcq_dp_test_start = False
lcq_dp_test(lcq_dp_test_start)

# Test cases for knapsack problems
knapsack_test_cases = [
    {"capacity": 165, "weights": [23, 31, 29, 44, 53, 38, 63, 85, 89, 82], "profits": [92, 57, 49, 68, 60, 43, 67, 84, 87, 72], "output": 309},
    {"capacity": 3, "weights": [4, 5, 6], "profits": [1, 2, 3], "output": 0},
    {"capacity": 4, "weights": [4, 5, 1], "profits": [1, 2, 3], "output": 3},
    {"capacity": 170, "weights": [41, 50, 49, 59, 55, 57, 60], "profits": [442, 525, 511, 593, 546, 564, 617], "output": 1735},
    {"capacity": 15, "weights": [4, 5, 6], "profits": [1, 2, 3], "output": 6},
    {"capacity": 15, "weights": [4, 5, 1, 3, 2, 5], "profits": [2, 3, 1, 5, 4, 7], "output": 19},
]

# KNAPSACK SOLUTIONS & KNAPSACK TESTS
def max_profit_recursive(capacity, weights, profits, idx=0):
    """Solves a knapsack problem (Trying to get maximum profit for minimum weights)"""
    # If we have processed all items, return 0
    if idx == len(weights):
        return 0
    # If the current items weight is greater than the weight capacity then skip it
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    # Else if the current item is not over capacity then either skip or add that item to the output, based on the value of the profit
    # If including item to output, then the capacity is subtracted from that items weight and moves on to the next item
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1), 
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))
    
def max_profit_recursive_test(start=False):
    """Test max_profit_recursive function via iterating through test cases and testing the functions output with the expected output"""
    if start == True:
        for idx, test in enumerate(knapsack_test_cases):
            fn_output = max_profit_recursive(test["capacity"], test["weights"], test["profits"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")    

max_profit_recursive_start = False
max_profit_recursive_test (max_profit_recursive_start)

def knapsack_memo(capacity, weights, profits):
    """Optimized version of max_profit_recursive using memoization to store and reuse results"""
    # Initilize memoization that stores results and reuses them.
    memo = {}

    # Recursive helper function
    def recurse(idx, capacity):
        key = (idx, capacity)
        # If a result of an item is already computed, then reuse and return it
        if key in memo:
            return memo[key]
        # If we have proccessed all items return 0 to be in the memoziation
        elif idx == len(weights):
            memo[key] = 0
        # If the currently selected items weight is over the capcacity then skip it
        elif weights[idx] > capacity:
            memo[key] = recurse(idx+1, capacity)
        # Else recursively compute algorithm by either adding or skipping the item based on the value of the profit
        # If adding then, the items profit is added to the output and the capacity is subtracted by the items weight
        else:
            memo[key] = max(recurse(idx+1, capacity), profits[idx] + recurse(idx+1, capacity-weights[idx]))

        # Return the result in the memoization for the current state
        return memo[key]
    # Start the algorithm at idx=0, as well as the capacity
    return recurse(0, capacity)

def knapsack_memo_test(start=False):
    """Test knapsack_memo function via iterating through test cases and testing the functions output with the expected output"""
    if start == True:
        for idx, test in enumerate(knapsack_test_cases):
            fn_output = knapsack_memo(test["capacity"], test["weights"], test["profits"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")    

knapsack_memo_start = False
knapsack_memo_test (knapsack_memo_start)

def knapsack_dp(capacity, weights, profits):
    """Implements knapsack solution but using dynamic programming of creating a table of size (w_length+1) by (capacity+1)"""
    # Initialize the length of weights
    w_length = len(weights)
    # Create a table with the dimensions (w_length+1) and (capacity+1) all initialized with zeros
    results = [[0 for _ in range(capacity+1)] for _ in range(w_length+1)]

    # Iterate through the weights
    for w_idx in range(w_length):
        # Iterate through the capacity values from 0 to capacity
        for c_idx in range(capacity+1):
            # If the current items weight is greater than the current capacity, then skip it
            if weights[w_idx] > c_idx:
                results[w_idx+1][c_idx] = results[w_idx][c_idx]
            # Else either add the currently selected item, or skip the currently selected item based on the value of the profit
            # If adding profit, then the capacity is decreased by the currently selceted items weight.
            else:
                results[w_idx+1][c_idx] = max(results[w_idx][c_idx], profits[w_idx] + results[w_idx][c_idx-weights[w_idx]])

    # Return the max profit for the full capacity for all items which is stored in the last cell of the table.
    return results[-1][-1]

def knapsack_dp_test(start=False):
    """Test knapsack_db function via iterating through test cases and testing the functions output with the expected output"""
    if start == True:
        for idx, test in enumerate(knapsack_test_cases):
            fn_output = knapsack_dp(test["capacity"], test["weights"], test["profits"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")    

knapsack_dp_start = True
knapsack_dp_test (knapsack_dp_start)