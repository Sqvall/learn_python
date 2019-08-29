class Circle:
    """Класс Circle"""
    all_circles = []  # Список экземпляров класса
    pi = 3.14159

    def __init__(self, r=1):
        if r <= 0:
            raise ValueError('Значение должно быть > 0')
        """Создать экземпляр класса с заданным значение radius"""
        self.radius = r
        self.__class__.all_circles.append(self)  # Добавить экземпляр в список экземпляров класса

    def area(self):
        """Вычислить площадь круга для экземпляра класса"""
        return self.radius ** 2 * self.__class__.pi

    def len_circle(self):
        """Вычислить длину окружности для экземпляра класса"""
        return self.__class__.pi * self.radius * 2

    @staticmethod
    def total_area():
        """Статический метод для вычисления площади всех Circle"""
        total = 0
        for i in Circle.all_circles:
            total += i.area()
        if total == 0:
            raise IndexError('В классе Circle отсутствуют экземпляры для суммирования')
        return total

    @classmethod
    def total_len_circle(cls):
        """Статический метод для вычисления длины окружни всех Circle"""
        total = 0
        for i in Circle.all_circles:
            total += i.len_circle()
        if total == 0:
            raise IndexError('В классе Circle отсутствуют экземпляры для суммирования')
        return total


c = Circle(2)
c2 = Circle(5)
c3 = Circle()

print(Circle.total_area())
print(Circle.total_len_circle())
