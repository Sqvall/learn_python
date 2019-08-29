a = [1, 2, 3, 4, 5, 's', [6, 4, 3, 2], 5.2]

a = a[::-1]

def reverse_args(*args):
    x = []
    [x.append(i) for i in args]
    x.reverse()
    return x


x = reverse_args(3, 4, 5, 44, [1, 6, 3], 'asd', a)
print(x)
# print(reverse_args(3, 4, 5, 44, [1, 6, 3], 'asd'))
