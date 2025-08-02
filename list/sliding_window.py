# Get max sub of sub_string
from functools import reduce

def get_max_sum_of_sub_string(lst, size):
    largest = window_sum = reduce(lambda x,y: x+y, lst[0:size])
    for i in range(size, len(lst)):
        window_sum = window_sum-lst[i-size]+lst[i]
        largest = largest if largest>window_sum else window_sum
    print(largest)


get_max_sum_of_sub_string([1,20,3,9,4,12,6],3)