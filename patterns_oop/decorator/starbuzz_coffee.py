from abc import ABC, abstractmethod


class Beverage(ABC):
    _description = "Unknown Beverage"

    def getDescription(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):
    @abstractmethod
    def cost(self):
        pass


class Espresso(Beverage):
    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return 1.99


class Decaf(Beverage):
    def __init__(self):
        self._description = "Decaf"

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.20


def main():
    only_espresso = Espresso()
    print(f"{only_espresso.getDescription()} ${only_espresso.cost():.2f}")

    beverage_1 = Espresso()
    beverage_1 = Mocha(beverage_1)
    beverage_1 = Mocha(beverage_1)
    beverage_1 = Soy(beverage_1)
    print(f"{beverage_1.getDescription()} ${beverage_1.cost():.2f}")

    beverage_2 = Decaf()
    beverage_2 = Soy(beverage_2)
    print(f"{beverage_2.getDescription()} ${beverage_2.cost():.2f}")


if __name__ == '__main__':
    main()
