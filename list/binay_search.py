# Given a sorted array of integers nums and an integer target, return the index of the target if
# it exists in the array. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

def binary_search(lst, key):
    start=0
    end = len(lst)-1
    while start<=end:
        mid = (start+end)//2
        if lst[mid]==key:
            return mid
        elif lst[mid]>key:
            end = mid-1
        elif lst[mid] < key:
            start = mid+1
    return -1

print(binary_search([1,2,3,4,5,6,7,8],8))


