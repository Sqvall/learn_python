from itertools import takewhile, dropwhile

values = [1, 4, 2, 2, 5, 6, 3, 4, 8]
predicate = lambda x: x < 5

# takewhile(func, iterable) - элементы до тех пор, пока func возвращает истину.
# takewhile(lambda x: x<5, [1, 4, 6, 4, 1]) --> 1 4
for elem in takewhile(predicate, values):
    print(elem)

print('-----')

# dropwhile(func, iterable) - элементы iterable, начиная с первого, для которого func вернула ложь.
# dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]) --> 6 4 1
for elem in dropwhile(predicate, values):
    print(elem)
