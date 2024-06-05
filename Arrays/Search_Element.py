def search_for_element(arr, length, target):
    # Your implementation here
    for i in range(length):
        if arr[i] == target:
            return i
    return -1


# Input:
# length = 8
# array data = 3 17 9 25 12 5 14 21
# target = 12

# Output:
# 4
