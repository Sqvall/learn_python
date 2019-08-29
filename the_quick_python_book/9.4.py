x = 5


def func_1():
    x = 3


def func_2():
    global x
    x = 2


func_1()
print(x)

func_2()
print(x)


t1 = lambda: 5+5
print(t1())
