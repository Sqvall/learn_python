my_list = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c', 'd', 'q']

for val in zip(my_list, my_list2):
    print(val)
print()

params = [
    [0, 2 ** 2],
    [2 ** 3, 2 ** 4]
]

data = zip(params)
for i in data:
    print(i)

print()

data = zip(*params)
for i in data:
    print(i)
