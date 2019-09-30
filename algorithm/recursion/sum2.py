def sum2(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum2(arr[1:])


print(sum2([1, 2, 3, 4]))
