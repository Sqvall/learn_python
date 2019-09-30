def countdown(number):
    print(number)
    if number <= 1:
        return
    else:
        countdown(number - 1)


countdown(5)
