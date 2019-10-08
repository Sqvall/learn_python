def double_inputs():
    while True:
        x = yield
        yield print(x * 2)


gen = double_inputs()

next(gen)       # run up to the first yield
gen.send(10)    # goes into 'x' variable

next(gen)       # run up to the next yield
gen.send(6)     # goes into 'x' again

next(gen)       # run up to the next yield
gen.send(94.3)  # goes into 'x' again
