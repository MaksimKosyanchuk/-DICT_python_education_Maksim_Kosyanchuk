"""Coffee types and their properties."""


class CoffeeMachineClass:
    """Coffee type and its properties."""
    water = 400
    milk = 540
    coffee_beans = 120
    cup = 9
    money = 550
    condition = "waiting"

    def my_replace(self, my_str):
        """delete " " from string"""
        my_str = my_str.replace(' ', '')
        return my_str


CoffeeMachineData = CoffeeMachineClass()


class Coffee:
    """Coffee class"""
    water: int
    milk: int
    coffee_beans: int
    price: int

    def __init__(self, _water, _milk, _coffee_beans, _price):
        self.water = _water
        self.milk = _milk
        self.coffee_beans = _coffee_beans
        self.price = _price


ESPRESSO = Coffee(250, 0, 16, 4)
LATTE = Coffee(350, 75, 20, 7)
CAPPUCCINO = Coffee(200, 100, 12, 6)
