class Rectangle:
    def __init__(self, width=0, length=0):
        self.side_width = width
        self.side_length = length
        try:
            if width == 0 or length == 0:
                raise ValueError('Вы должны задать значение обеим сторона прямоугольника')
            if width < 0 or length < 0:
                raise Exception('Заданные значения должны быть больше 0')
        except ValueError as error:
            print(error)
            pass

    def area(self):
        return self.side_width * self.side_length


rec = Rectangle(width=6, length=2)
print(f"If length: {rec.side_length} and width: {rec.side_width}\nSquare rectangle: {rec.area()}")
print('------')
rec = Rectangle(10, 5)
print(f"If length: {rec.side_length} and width: {rec.side_width}\nSquare rectangle: {rec.area()}")
