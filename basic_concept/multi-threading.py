import time
import threading

def calcu_sqr(lst):
    for num in lst:
        time.sleep(0.2)
        print(f"Squire of {num} is:{num*num}")

def calcu_cube(lst):
    for num in lst:
        time.sleep(0.2)
        print(f"Cube of {num} is:{num*num*num}")


t = time.time()
lst = [2,3,4,5]
thread1 = threading.Thread(target=calcu_sqr, args=(lst,))
thread2 = threading.Thread(target=calcu_cube, args=(lst,))
# calcu_sqr(lst)
# calcu_cube(lst)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Total time taken by function:{time.time()-t}")