def fun1(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return print(b + x)

    return fun2


test_fun = fun1(4)
test_fun(7)
