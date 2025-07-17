#Selection sort
def sort_lst(lst):
    for i in range(len(lst)):
        min_idx = i # for finding min element index
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i] # swapping no
    return lst

sorted_list = sort_lst([3,2,4,5,1])
print(sorted_list)