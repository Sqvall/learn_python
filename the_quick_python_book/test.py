from tags import *


# x = [1]
# x.append(2)
# x.append([3,4])
# print('The list x is ' + repr(x))

# class C:
#     print(locals().keys())
#     print(globals().keys())
#
#     def print_s(self):
#         print(dir(self))
#         print(globals().keys())
#         print("loc", locals().keys())

class New(Tags):
    # print('GLOB', list(globals().keys()))
    # print('LOCAL', list(locals().keys()))
    print(Tags.__class__)


# print(New.__class__.__dict__)
# a = New()
# print(a.__dir__())
# print(a.x)
def qwe():
    x = 1
    y = 4
    z = []
    print(z)
    def print_x():
        z.append(312)
        nonlocal y
        y = 5
        q = (print(x))
    print_x()

    print(z)
    print(y)
    pass


qwe()
