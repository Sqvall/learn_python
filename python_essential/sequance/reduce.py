from functools import reduce

values = [4, 5, 2, 2, 2.5]
product = reduce(lambda x, y: x * y, values)  # 4 * 5 = 20 * 2 = 40 * 2 = 80 * 2.5 = 200.0

print(product)
