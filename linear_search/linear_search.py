# Simple Linear Search Algorithm that traverses through an array of cards, and returns the index that the target card was in
def locate_card(cards, target):
    # Start with a position of 0
    idx = 0
    # Iterate through each card
    for card in cards:
        # If the card is equal to the target, return its index/position
        if card == target:
            return idx
        
        # Move on to the next card
        idx += 1

    # Return -1 if no target card was found
    return -1

# LIST OF TEST CASES TO EVALUATE FUNCTION
test_cases = [
    {"input": [13, 11, 10, 7, 4, 3, 1, 0], "target": 7, "output": 3},
    {"input": [13, 11, 10, 7, 4, 3, 1, 0], "target": 1, "output": 6},
    {"input": [4, 2, 1, -1], "target": 4, "output": 0},
    {"input": [3, -1, -9, -127], "target": -127, "output": 3},
    {"input": [6], "target": 6, "output": 0},
    {"input": [9, 7, 5, 2, -9], "target": 4, "output": -1},
    {"input": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "target": 3, "output": 7},
    {"input": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "target": 6, "output": 2},
]

# Function that goes through the test cases and evaluates the locate_card function
def locate_card_test(start=False):
    """Iterates through the test_cases list and comapres the input with the expected output, print statements if output and expected outputs do/do not match"""
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = locate_card(test["input"], test["target"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

locate_card_test_start = True
locate_card_test(locate_card_test_start)