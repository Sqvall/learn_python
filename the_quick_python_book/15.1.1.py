class Circle:
    pass


my_circle = Circle()
my_circle.radius = 5
print(int((2 * 3.14 * my_circle.radius)*100)/100, end="\n-------------------------\n")


class Circle:
    def __init__(self):
        self.radius = 1


my_circle = Circle()
print(int((2 * 3.14 * my_circle.radius)*100)/100)
my_circle.radius = 5
print(int((2 * 3.14 * my_circle.radius)*100)/100)
print(Circle().radius)
