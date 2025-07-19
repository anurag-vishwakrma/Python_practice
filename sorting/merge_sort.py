from typing import List

def merge_list(lst1:List[int], lst2:List[int]) ->List[int]:
    final_lst = []
    i,j = 0,0
    while i < len(lst1) and j < len(lst2):
        if lst1[i]>lst2[j]:
            final_lst.append(lst2[j])
            j = j+1
        else:
            final_lst.append(lst1[i])
            i=i+1

    while i < len(lst1):
        final_lst.append(lst1[i])
        i = i + 1

    while j < len(lst2):
        final_lst.append(lst2[j])
        j = j+1
    return final_lst

def merge_sort(lst:List[int]) -> List[int]:
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge_list(left, right)


if __name__ == '__main__':
    # print(merge_list([1,3,5,7],[2,4,6,8]))
    print(merge_sort([5,"2",4,3,8]))