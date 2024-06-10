def find_unique_magical_key(arr, length):
    Map = {}
    for i in arr:
        if i in Map:
            Map[i] += 1
        else:
            Map[i] = 1
    
    for key, count in Map.items():
        if count == 1:
            return key
    
    return -1




# Example:
# Input:
# 10
# 7 12 4 9 3 7 13 9 4 12 3
# Output:
# 13

