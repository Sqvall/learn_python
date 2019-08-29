class User:
    def __init__(self, name: str, surname=None, patronymic=''):
        surname_list = [surname]
        self.__name = name
        self.__surname = surname_list
        self.__patronymic = patronymic
        self.__initial = self.__get_initial()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Name it's requirement argument")
        self.__name = new_name
        self.__initial = self.__get_initial()

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if not new_surname:
            raise ValueError("Surname it's requirement argument")
        self.__surname = new_surname
        self.__initial = self.__get_initial()

    def add_surname(self, new_surname):
        if not new_surname:
            raise ValueError("Surname it's requirement argument")
        self.__surname.append(new_surname)
        self.__initial = self.__get_initial()

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, new_patronymic):
        self.__patronymic = new_patronymic
        self.__initial = self.__get_initial()

    @property
    def initial(self):
        return self.__initial

    def __get_initial(self):
        if not self.__patronymic:
            return self.__name[0].upper() + '. ' + self.__surname[-1]
        else:
            return self.__name[0].upper() + '.' + self.__patronymic[0].upper() + '. ' + self.__surname[-1]

    def __str__(self):
        return str('Фамилия: ' + self.surname[-1] +
                   '\nИмя: ' + self.name +
                   '\nОтчество: ' + self.patronymic +
                   '\nИнициалы: ' + self.initial)


u1 = User("Анатолий", "Петров", "Витальевич")
u1.add_surname('Кракотец')
# u1.name = ''
# u1.surname = ''
u1.patronymic = ''
print(u1)
