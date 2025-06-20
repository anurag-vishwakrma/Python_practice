"""Given a list of integers and a rotation count, rotate the list to the left by the given number of
    positions without using extra space.
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rotation_count = 5

    Output:
        [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]"""

def rotate_list(lst,rotation_count):
    for i in range(0,rotation_count):
        tmp= lst[-1]
        for pos in range(len(lst)-1,0, -1):
            lst[pos]=lst[pos-1]
        lst[0]=tmp
    return lst

if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rotation_count = 5
    result = rotate_list(input_list, rotation_count)
    print("Rotated List:", result)