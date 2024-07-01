# Test Cases that will be used to test functions that mutiply polynomials
test_cases = [
    {"poly1": [2, 0, 5, 7], "poly2":[3, 4, 2], "output": [6, 8, 19, 41, 38, 14]},
    {"poly1": [7, 8, 2], "poly2":[8, 6, 5], "output": [56, 106, 99, 52, 10]},
    {"poly1": [8, 4, 6], "poly2":[2, 6, 7], "output": [16, 56, 92, 64, 42]},
    {"poly1": [3, 1], "poly2":[1, 4], "output": [3, 13, 4]},
    {"poly1": [5, 2], "poly2":[1, 4], "output": [5, 22, 8]},
    {"poly1": [2, 5], "poly2":[3, 4], "output": [6, 23, 20]},
]

def multiply(poly1, poly2):
    """Basic Implemenation of algorithm that can solve polynomial equations"""
    # Find the length of poly1 and poly2
    poly1_size, poly2_size = len(poly1), len(poly2)
    # Figure out the size of the resulting list by doing poly1_size + poly2_size - 1
    result_size = poly1_size + poly2_size - 1
    # Populate the resulting list with all zeros of size poly1_size + poly2_size - 1 
    result = [0] * result_size
    # Initialize indices to iterate through both polynomials
    i, j, = 0, 0
    # Iterate through both polynomails and mutiply corresponding elements
    for i in range(poly1_size):
        for j in range(poly2_size):
            result[i + j] += poly1[i] * poly2[j]

    # Return the result
    return result

def multiply_test(start=False):
    """Test multiply function by comparing its output with the expected one"""
    if start == True:
        for idx, test in enumerate(test_cases):
            fn_output = multiply(test["poly1"], test["poly2"])
            if fn_output == test["output"]:
                print(f"Test {idx + 1}: True")
            else:
                print(f"Test {idx + 1}: False - Expected Output: {test['output']}, got {fn_output}")

multiply_test_start = True
multiply_test(multiply_test_start)