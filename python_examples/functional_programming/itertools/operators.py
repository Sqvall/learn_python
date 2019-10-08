""" https://docs.python.org/3.7/library/operator.html """

from functools import reduce
from operator import neg, mul

values = [1, 5, 2, -4, -2, 3]
print(list(map(lambda x: -x, values)))
print(list(map(neg, values)))

print('===')

values = [4, 5, 2, 2, 2.5]
print(reduce(lambda x, y: x * y, values))   # 4 * 5 = 20 * 2 = 40 * 2 = 80 * 2.5 = 200.0
print(reduce(mul, values))                  # 4 * 5 = 20 * 2 = 40 * 2 = 80 * 2.5 = 200.0
