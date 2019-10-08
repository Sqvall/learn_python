def decorator(fn):
    def decorated_fn(*args, **kwargs):
        print('Starting decorated function')
        print('*' * 10)
        print(args[0] + args[1])
        print('*' * 10)
        fn(*args, **kwargs)
        print('End of decorated function')

    return decorated_fn


@decorator
def print_hello(*args):
    print()
    print('args:', *args)
    print()
    print('Hello')


print_hello(1, 3)
