# Insertion sort

def sort_lst(lst):
    for i in range(1,len(lst)):
        for j in range(0, i-1):
            if lst[j]>lst[i]:
                lst[j], lst[i] = lst[i], lst[j] # swapping no
    return lst

sorted_list = sort_lst([3, 2, 4, 5, 1, 3])
print(sorted_list)