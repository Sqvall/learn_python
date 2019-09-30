import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def smallest_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(smallest_sort([1, 13, 3, 53, 9, 111]))

print('*' * 25)

print(len([i + random.randint(1, 100) for i in range(1, 50)]))
print([i + random.randint(1, 100) for i in range(1, 50)])

print(len(smallest_sort([i + random.randint(1, 100) for i in range(1, 50)])))
print(smallest_sort([i + random.randint(1, 100) for i in range(1, 50)]))
