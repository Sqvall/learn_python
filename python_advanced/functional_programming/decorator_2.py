def decorator(fn):
    print("Decorate function name: " + fn.__name__)
    return fn


@decorator
def print_hello(*args):
    print(*args)
    print('Hello')


print_hello(1, 2)
