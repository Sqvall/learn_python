import numpy

value1 = numpy.arange(1, 20)
print(value1)

value2 = numpy.arange(0, 20, 5)
print(value2)

value3 = numpy.arange(20, 0, -5)
print(value3)

value4 = numpy.linspace(1, 5, 20)
print(value4)

value5 = numpy.linspace(1, 5, 9, dtype=numpy.int8)
print(value5)

value6 = numpy.random.randint(1, 100, 10)
print(value6)

value7 = numpy.random.rand(3, 4)
print(value7)

