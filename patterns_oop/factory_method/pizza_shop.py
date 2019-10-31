from abc import ABC, abstractmethod


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    topping: list

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for i in self.topping:
            print("    " + i)

    @staticmethod
    def bake():
        print("Bake for 25 minutes at 350")

    @staticmethod
    def cut():
        print("Cutting the pizza into diagonal slices")

    @staticmethod
    def box():
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name


class PizzaStore(ABC):
    menu = {}

    def order_pizza(self, pizza_type: str):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.topping = []
        self.topping.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.topping = []
        self.topping.append("Shredded Mozzarella Cheese")


class NYPizzaStore(PizzaStore):
    def __init__(self):
        self.menu = {
            "cheese": NYStyleCheesePizza()
        }

    def create_pizza(self, pizza_type):
        return self.menu[pizza_type]


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self.menu = {
            "cheese": ChicagoStyleCheesePizza()
        }

    def create_pizza(self, pizza_type):
        return self.menu[pizza_type]


def main():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}\n")


if __name__ == '__main__':
    main()
