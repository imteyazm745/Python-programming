# Python program to interchange first and last elements in a list.

"""Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]"""

# Approach 1: swap first and last elements
def swapList(list):
    size = len(list)
    
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = temp
    
    return list

list = [15, 40, 5, 97, 21]
print(swapList(list))

# Approach 2: swap first and last elements
def swappingList(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1

list1 = [15, 40, 5, 97, 21]
print(swappingList(list1))

# Approach 3: swap first and last elements
def swapList2(list2):
    get = list2[-1], list2[0]
    list2[0], list2[-1] = get
    return list2

newlist2 = [15, 40, 5, 97, 21]
print(swapList2(newlist2))