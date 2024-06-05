# Problem Statement:
# The task is to find the nth number in the Fibonacci series.
# The Fibonacci series is defined as follows: the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding numbers. The series begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.

# Constraints:
# 0 <= n <= 40
# Input Format:
# An integer, 'n', representing the position of the desired Fibonacci number.
# Output Format:
# An integer, the nth Fibonacci number.
# Sample Examples:

# 1.
# Input: 6
# Output: 5
# Explanation: The 6th Fibonacci number is 5.

# 2.
# Input: 9
# Output: 21
# Explanation: The 9th Fibonacci number is 21.


def print_series(n):
    """write code here""" 
    if n <= 0:
        return 0
    if n == 1:
        print(0)
        return
    
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    
    print(series[-1])