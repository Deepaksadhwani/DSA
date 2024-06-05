def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Problem Statement:
# An integer 'N' for which the factorial needs to be calculated.
# Sample Examples:
# 1.
# Input: 5
# Output: 120
# Explanation: The factorial of 5 is calculated as 5 * 4 * 3 * 2 * 1 = 120.

# 2.
# Input: 8
# Output: 40320
# Explanation: The factorial of 8 is calculated as 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320.
