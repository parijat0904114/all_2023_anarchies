# Imagine you have an unsorted list of n numbers. The goal is to find out
# the position/index of a specific number x. What can you do? Check numbers one by one.
# If the number you are looking is at the last position, then you have to check all the
# n numbers. So, worst case complexity is O(n). Best case complexity would be O(1). The first
# number in the list is the number you are looking for. This is LINEAR SEARCH.

def linear_search(array, x):
    for i, n in enumerate(array):
        if n == x:
            return i
    return None

arr = [4,2,5,6,7,3,1,11]
print(linear_search(arr, 3))
print(linear_search(arr, 42))

# Binary Search...
def binary_search(array, key):
    begin = 0
    end = len(array) - 1
    index = None
    while(begin<=end):
        mid = int((begin+end)/2)
        if array[mid]==key:
            index=mid
            break
        elif key>array[mid]:
            begin = mid + 1
        elif key<array[mid]:
            end = mid - 1
    return index

a = [1,3,4,6,9,14,17,24]
print(binary_search(a, 6))