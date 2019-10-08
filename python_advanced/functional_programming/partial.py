# Частичное приминение функции(вызов функции с меньшим количеством аргументов, чем она ожидает, и получение
# функции, которая принимает оставшиеся параметры)

from functools import partial

print_with_comma = partial(print, sep=', ')
print_with_comma(1, 2, 3, 'hello')
