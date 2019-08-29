import datetime
import time

def test():
    x = time.time()
    global r
    r = 0
    for i in range(0, 10000):
        for j in range(0, 10000):
            r = (r + (i * j) % 100) % 47
    print(time.time() - x)


test()
print("answer: ", r)
