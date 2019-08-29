class ValueTooLarge(Exception):
    pass


try:
    x = int(input('Введите целое число не больше 1000\n'))
    if x > 1000:
        raise ValueTooLarge('Введёное число больше 1000!!!')
except ValueTooLarge as error:
    print(error)
    # print('Число больше 1000')
