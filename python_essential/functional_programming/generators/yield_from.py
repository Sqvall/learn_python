# TEST 1
# def generator():
#     yield from range(3)
#     yield 'end'
#
#
# for value in generator():
#     print(value)


# TEST 2
print('*' * 10)
def subgenerator():
    yield '[subgenerator] start'
    print('simply print before end subgenerator')
    yield '[subgenerator] end'


def generator():
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]    end'


q = generator()

print(next(q))
print(next(q))
print(next(q))

# for value in generator():
#     print(value)
# print('*'*10)

# TEST 3
# def generator():
#     yield range(10)
#     yield 'end'
#
#
# for value in generator():
#     print(value)
#
