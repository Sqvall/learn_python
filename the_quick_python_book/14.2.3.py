""" Делит первое введённое число на второе """
try:
    x = int(input('Введите делимое число\n'))
    y = int(input('Введите делитель\n'))
    try:
        print(x / y)
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    except ValueError:
        print("Введёноё число должно быть 'целым'")

except ValueError:
    print('Введите целое число')
