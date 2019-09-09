import time

STOP = 1000000 ** 1000
start = time.time()


def fibonacci():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second
        if first >= STOP:
            print(int((time.time() - start) * 1000))
            break


f = fibonacci()
try:
    while True:
        print(next(f), end='\n\n')
except StopIteration:
    print("It's all")
