try:
    x = int(input('Введите целое число больше 0\n'))
    assert x > 0, "Введённое число должно быть положительным и больше 0"
    print(x)
except ValueError:
    print('Введён не верный тип данных')
