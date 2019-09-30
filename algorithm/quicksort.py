import random


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(greater)


print(qsort([4, 44, 6, 3, 7, 5, 2]))

print('*' * 25)

print(len([i + random.randint(1, 100) for i in range(1, 50)]))
print([i + random.randint(1, 100) for i in range(1, 50)])

print(len(qsort([i + random.randint(1, 100) for i in range(1, 50)])))
print(qsort([i + random.randint(1, 100) for i in range(1, 50)]))
