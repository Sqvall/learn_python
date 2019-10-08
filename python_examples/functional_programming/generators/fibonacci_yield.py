def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = int(input('How many Fibonacci numbers to print?'))

fib = fibonacci(count)
while True:
    try:
        print(next(fib))
    except StopIteration:
        print('End')
        break
