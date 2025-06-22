"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target"""

# def twosum(nums, target):
#     for i in range(0,len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
#     return [0,0]

def twosum(nums, target):
    num_map = {}  # Store value: index
    for i, num in enumerate(nums,start=0):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return [0,0]

print(twosum([1,2,3,4],7))