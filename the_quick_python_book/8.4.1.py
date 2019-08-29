x = [1, 3, 5, 0, -1, 3, -2]
[x.remove(i) for i in x if i < 0]
print(x)

x = [i for i in range(101) if i % 2]
print(x)

x = {i: i ** 3 for i in range(15, 11-1, -1)}
print(x)
