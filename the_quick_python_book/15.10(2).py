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
    qwe = 333
    def __init__(self, s_x=1, s_y=1, x=0, y=0):

        # Shape.__init__(self, x, y)
        super().__init__(x, y)

        self.__side_x = s_x
        self.__side_y = s_y

    @property
    def side_x(self):
        return self.__side_x

    @side_x.setter
    def side_x(self, new_x):
        if new_x >= 0:
            self.__side_x = new_x

    @property
    def side_y(self):
        return self.__side_y

    @side_y.setter
    def side_y(self, new_y):
        if new_y >= 0:
            self.__side_y = new_y

Rectangle.qwe = 111
print(Rectangle.qwe)
r = Rectangle(2, 3)
print(r.side_x, ':', r.side_y)
r.side_x = 5
r.side_y = 1
# r.x, r.y = 1, 2
print(r.side_x, ':', r.side_y)
print(r.qwe)
print(r.__dict__)
