# Closure - замыкание

# This we need
# def mul(a, b):
#     return print(a * b)
#
#
# def mul5(a):
#     return mul(5, a)
#
#
# mul5(2)
# mul5(7)


def mul(a):

    def helper(b):
        return print(a * b)

    return helper


mul(5)(2)
print('*' * 8)
new_mul5 = mul(5)
new_mul5(3)
