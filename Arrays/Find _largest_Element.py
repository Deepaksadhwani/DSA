





def find_maximum(nums):
    Highest = float("-inf") 
    for i in nums:
        if i > Highest:
            Highest = i
    return Highest




# Example:
# Input:
# 5
# 12 7 31 18 25
# Output:
# 31