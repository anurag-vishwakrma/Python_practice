import multiprocessing
import time

def cal_sqr(lst, result):
    for idx,num in enumerate(lst):
        # time.sleep(1)
        # result.append(num*num)
        result[idx] = num*num
        # print(f"Squire of {num} is:{num*num}")
    print(f"Result inside process{result}")

def cal_cube(lst):
    for num in lst:
        time.sleep(2)
        print(f"Cube of {num} is:{num*num*num}")


lst = [2,3,4,5,6]
result = multiprocessing.Array('i', 5)
process1 = multiprocessing.Process(target=cal_sqr, args=(lst,result))

process2 = multiprocessing.Process(target=cal_cube, args=(lst,))

process1.start()
process2.start()

process1.join()
print(result[:])
process2.join()