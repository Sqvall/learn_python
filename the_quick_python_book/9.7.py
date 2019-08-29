def four(start=0, limit=4):
    start = start
    while start < limit:
        print('in generator, start =', start)
        yield start
        start += 1


for i in four(2):
    print(i)
