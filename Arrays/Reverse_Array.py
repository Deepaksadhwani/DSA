
    # straight loop
def reverse_array(arr, length):
    reverse_arr = []
    for i in range(1, length + 1):
        reverse_arr.append(arr[-i])
    return reverse_arr

#    reverse loop
def reverse_array(arr, length):
    reverse_arr = []
    for i in range(length - 1, -1, -1):
        reverse_arr.append(arr[i])
    return reverse_arr


# Input:
# 6
# 17 32 9 5 21 14
# Output:
# 14 21 5 9 32 17