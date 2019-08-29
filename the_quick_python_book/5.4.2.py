l = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]


def sort_second_element(x: list):
    x = x[1]
    return x


# print(sort_second_element(l))
l.sort(key=sort_second_element)
print(l)
