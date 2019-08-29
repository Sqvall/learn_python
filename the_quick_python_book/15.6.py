class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Circle(Shape):
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r


class Square(Shape):
    def __init__(self, s=1, x=0, y=0):
        super().__init__(x, y)
        self.side = s

    def square(self):
        square = self.side ** 2
        return square


class Rectangle(Shape):
    def __init__(self, s_y=1, s_x=1, x=0, y=0):
        super().__init__(x, y)
        self.side_x = s_x
        self.side_y = s_y


x = Rectangle(2, 6)
x.move(delta_x=-6, delta_y=9)

s = Square(5)

print(f'Square: {s.square()} /', s.__str__())
print(x.__dict__)
