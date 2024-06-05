def sumOfMultiples(n,x):
    loop_duration = n // x
    Sum = 0
    for i in range(loop_duration):
        Sum += x * (i + 1) 
       
    return Sum

# Problem Statement:
# Calculate the sum of all numbers between 1 and N (inclusive) that are multiples of a given integer X.

# Constraints:
# 1 <= N <= 10^5
# 1 <= X <= N
# Input Format:

# Two integers, N and X, separated by a space. N represents the upper limit of the range, and X represents the integer whose multiples need to be summed.
# Output Format:
# An integer representing the sum of all numbers between 1 and N that are multiples of X.

# Sample Examples:
# 1.
# Input: N = 10, X = 3
# Output: 18
# Explanation: The multiples of 3 between 1 and 10 are 3, 6, and 9. The sum of these multiples is 3 + 6 + 9 = 18.

# 2.
# Input: N = 20, X = 4
# Output: 60
# Explanation: The multiples of 4 between 1 and 20 are 4, 8, 12, and 16. The sum of these multiples is 4 + 8 + 12 + 16 = 40.