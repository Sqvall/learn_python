class Character:
    def __init__(self):
        self.health = None
        self.weapon = None

    def set_weapon(self, weapon):
        print("I'm change weapon on: " + weapon.__class__.__name__.lower())
        self.weapon = weapon

    def use_weapon(self):
        self.weapon.use_weapon()

    def display(self):
        raise NotImplementedError


class Warrior(Character):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.weapon = Sword()

    def display(self):
        print('*' * 15,
              f"\nI'm a {self.__class__.__name__}",
              f"\nHealth: {self.health}\n" + '*' * 15)


class WeaponBehavior:
    def use_weapon(self):
        raise NotImplementedError


class Sword(WeaponBehavior):
    def use_weapon(self):
        print('Hit:', 'swing', '(' + self.__class__.__name__.lower() + ')')


class Dagger(WeaponBehavior):
    def use_weapon(self):
        print('Hit:', 'backstab', '(' + self.__class__.__name__.lower() + ')')


war = Warrior()
war.display()
war.use_weapon()

war.set_weapon(Dagger())
war.use_weapon()

