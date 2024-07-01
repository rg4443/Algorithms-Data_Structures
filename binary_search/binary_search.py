def locate_side(cards, query, middle):
    """Helper function that helps locate which side of the cards need to be searched next, returns "found" if the target card is found"""
    middle_num = cards[middle]
    if middle_num == query:
        if cards[middle - 1] == query and middle - 1 >= 0:
            return "left"
        return "found"
    elif middle_num > query:
        return "right"
    else: # middle_num < query
        return "left"

def locate_card(cards, query):
    """Function that locates a target card from a list of cards via inputs of a list and the target card"""
    # Define the size of indices for the array of cards
    low_indice = 0
    high_indice = len(cards) - 1

    while low_indice <= high_indice:
        middle_card = (low_indice + high_indice) // 2
        side = locate_side(cards, query, middle_card)
        if side == "found":
            return middle_card
        # Search first half of list
        elif side == "left":
            high_indice = middle_card - 1
        # Search second half of list
        else:
            low_indice = middle_card + 1

    # Query was not found in cards
    return -1

# Test cases to test functions
test_cases = [
    {"input": [13, 11, 10, 7, 4, 3, 1, 0], "query":7, "output": 3},
    {"input": [13, 11, 10, 7, 4, 3, 1, 0], "query":1, "output": 6},
    {"input": [4, 2, 1, -1], "query":4, "output": 0},
    {"input": [3, -1, -9, -127], "query":-127, "output": 3},
    {"input": [6], "query":6, "output": 0},
    {"input": [9, 7, 5, 2, -9], "query":4, "output": -1},
    {"input": [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query":3, "output": 7},
    {"input": [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], "query":6, "output": 2},
]

def locate_card_test(start=False):
    """Test function that test all of the test cases on the locate_card function"""
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = locate_card(test["input"], test["query"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

locate_card_test_start = True
locate_card_test(locate_card_test_start)