# bubble sort
# Repeatedly swapping adjacent elements
# The largest values "bubble up" to the end of the list in each pass.

def sort_lst(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j+1]<lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1] # swapping no
    return lst

sorted_list = sort_lst([3,2,4,5,1,3])
print(sorted_list)