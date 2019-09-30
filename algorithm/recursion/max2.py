def max2(arr: list):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max2(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(max2([2, 33, 44, 22, 14, 53, 6, 36, 53, 23, 55]))
