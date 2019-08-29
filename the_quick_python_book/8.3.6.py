z = [1, 3, 5, 0, -1, 3, -2]

for x, y in enumerate(z):
    if y < 0:
        del z[x]

print(z)

z = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]

count = 0
for i in z:
    for q in i:
        if q < 0:
            count += 1

print(count)

