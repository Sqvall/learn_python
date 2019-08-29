def decorate(func):
    def wrapper_func(*args):
        for i in args:
            print('<html>', i, '</html>', sep='')

    return wrapper_func


@decorate
def myfunction(*args):
    x = 1  # print(parameter)


myfunction('Hello', 'as', 2, ['qwe', 3, 5.5])
