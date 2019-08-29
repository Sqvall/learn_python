class TypedList(list):
    def __init__(self, element, initial_list=None):
        if initial_list is None:
            initial_list = []
        self.type = type(element)
        if not isinstance(initial_list, list):
            raise TypeError(f"Второй аргумент в классе {self.__class__.__name__} должен быть список")
        for elem in initial_list:
            self.__check(elem)
        super().__init__(initial_list)

    def __check(self, argument):
        if type(argument) != self.type:
            raise TypeError(f"Вы пытаетесь добавить элемент неверного типа")

    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)


x = TypedList('', 5 * [''])
x[2] = 'Hello'
x[3] = 'There'
print(x[2] + ' ' + x[3])

a, b, c, d, e = x
print(a, b, c, d)
print(x)
y = x[:]
print(y)
del y[2]
print(y)
y.sort()
print(y)
x.sort()
print(x)
q = TypedList(5, [])
q.append(8)
q.append(8)
q.append(8)
q.append('8')
print(q.type)
