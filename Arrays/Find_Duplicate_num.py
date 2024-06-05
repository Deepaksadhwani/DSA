def find_first_duplicate_element(arr):
    Map = {}
    for num in arr:
        if num in Map:
            return num
        Map[num] = True
    return -1

# for loop = O(n)
# search in hash map is constant O(1)
# Time Complexity: O(n)
# Space Complexity: O(n)



def find_first_duplicate_element(arr):
    temp_list = []
    for i in arr:
        if i in temp_list:
            return i
        temp_list.append(i)
    return -1

#  for loop = first O(n)
#  "in in if condition is also on as Search which is array second O(n) " 
# Time Complexity: O(n^2)
# Space Complexity: O(n)