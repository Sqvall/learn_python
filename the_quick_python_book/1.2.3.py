def pairwise_sum(list1, list2):
    result = []
    for i in range(len(list1)):
        # print(i)
        result.append(list1[i] + list2[i])
        print(result)
    return result


a = [6, 2, 3]
b = [4, 5, 6]

print(pairwise_sum(a, b))


