"""
You are given an array nums consisting only of integers 0, 1, and 2. Write an algorithm to sort the array in-place so that all 0s come first, followed by all 1s and then all 2s.

You must solve this problem in one pass (O(n) time complexity) using constant space (O(1) space complexity).

"""

def sort_list(lst):
    low, mid, high = 0,0,len(lst)-1
    while mid<=high:
        if lst[mid]>1:
            lst[mid],lst[high] = lst[high], lst[mid]
            high = high -1
        elif lst[mid]<1:
            lst[mid], lst[low] = lst[low], lst[mid]
            low = low+1
            mid = mid+1
        else:
            mid = mid+1
    return lst

print(sort_list([2,1,2,0,0,2,1]))
