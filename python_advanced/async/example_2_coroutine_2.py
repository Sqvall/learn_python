# Infinity send
import random


def is_divider(number):
    print("Coroutine started")
    while True:
        value = yield
        if number % value == 0:
            print(value)


cor = is_divider(100)
cor.send(None)


while True:
    x = int(input('Integer number: '))
    # x = random.randint(1, 100)
    cor.send(x)
