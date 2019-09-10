values = [1, 2, 3, 4, 5, 6, 7, 8]

squares = list(map(lambda x: x ** 2, values))
print(squares)

for square in map(lambda x: x ** 2, values):
    # print(square)
    pass
