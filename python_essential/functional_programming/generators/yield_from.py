"""
В Python 3 существуют так называемые подгенераторы (subgenerators).
Если в функции-генераторе встречается пара ключевых слов yield from,
после которых следует объект-генератор, то данный генератор делегирует
доступ к подгенератору, пока он не завершится (не закончатся его значения),
после чего продолжает своё исполнение.
"""


def generator():
    yield from (3 * x for x in range(4))
    print()
    yield from (2 * x for x in range(5, 8))


for i in generator():
    print(i)


# TEST 1
# def generator():
#     yield from range(3)
#     yield 'end'
#
#
# for value in generator():
#     print(value)


# TEST 2
def subgenerator():
    yield '[subgenerator] start'
    print('simply print before end subgenerator')
    yield '[subgenerator] end'


def generator():
    print('*' * 30)
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]    end'


q = generator()

print(next(q))
print(next(q))
print(next(q))

# for value in generator():
#     print(value)


# TEST 3
# def generator():
#     print('*'*10)
#     yield range(10)
#     yield 'end'
#
#
# for value in generator():
#     print(value)

