from abc import ABC, abstractmethod


class BeverageWithHook(ABC):
    def prepare_recipe(self):
        """ Template method!!! """
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @staticmethod
    @abstractmethod
    def brew():
        pass

    @staticmethod
    @abstractmethod
    def add_condiments():
        pass

    @staticmethod
    def boil_water():
        print("Boiling water")

    @staticmethod
    def pour_in_cup():
        print("Pouring in cup")

    @staticmethod
    def customer_wants_condiments():
        return True


class CoffeeWithHook(BeverageWithHook):
    @staticmethod
    def brew():
        print("Dripping Coffee through filter")

    @staticmethod
    def add_condiments():
        print("Adding Sugar and Milk")

    @staticmethod
    def customer_wants_condiments():
        answer: str = input("Would you like milk and sugar with your coffee (y/n)? ")

        if answer.startswith("y"):
            return True
        return False


class TeaWithHook(BeverageWithHook):
    @staticmethod
    def brew():
        print("Steeping the tea")

    @staticmethod
    def add_condiments():
        print("Adding Lemon")

    @staticmethod
    def customer_wants_condiments():
        answer: str = input("Would you like lemon with your tea (y/n)? ")

        if answer.startswith("y"):
            return True
        return False


if __name__ == '__main__':
    coffee_hook = CoffeeWithHook()
    print("\nMaking coffee...")
    coffee_hook.prepare_recipe()

    tea_hook = TeaWithHook()
    print("\nMaking tea...")
    tea_hook.prepare_recipe()
