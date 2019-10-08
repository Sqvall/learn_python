from itertools import product, chain

# Origin
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(f"{i} x {j} = {i * j}")

# Analog with product
for i, j in product(range(1, 5), range(1, 5)):
    print(f"{i} x {j} = {i * j}")

# Chained iteration
for i in chain(range(1, 10), range(1, 5)):
    print(i)
