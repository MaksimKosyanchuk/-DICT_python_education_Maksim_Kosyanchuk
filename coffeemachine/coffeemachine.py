"""Coffee Machine script"""
from classes import CoffeeMachineData
from classes import ESPRESSO
from classes import LATTE
from classes import CAPPUCCINO

WHAT_DO_YOU_WANT = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu: \n> "  # pylint: disable=C0301
MAKE_COFFEE = "I have enough resources, making you a coffee!"
ALL_COFFEE = {1: "espresso", 2: "latte", 3: "cappuccino"}


class CoffeeMachine:
    """Coffee Machine class"""
    condidion = "waiting"
    def coffee_machine_has(self):
        """Coffee machine has func"""
        machine_has = f"""Coffee Machine has:
                {CoffeeMachineData.water} of water
                {CoffeeMachineData.milk} of milk
                {CoffeeMachineData.coffee_beans} of coffee beans
                {CoffeeMachineData.cup} of disposable cups
                {CoffeeMachineData.money} of money    
                """
        print(machine_has)

    def check_user_input(self, user_input):
        """Проверить ввод пользователя, user_input - int выбора пользователя, возвращает False, если надо выйти с программы"""
        condition = user_input
        match condition:
            case "buy":
                self.user_buy()
                return True
            case "fill":
                self.user_fill()
                return True
            case "take":
                self.user_take()
                return True
            case "remaining":
                self.coffee_machine_has()
                return True
            case "exit":
                return False

    def my_input(self):
        """User input func, возвращает int выбора пользователя"""
        iterator_var = True

        def check_input():
            if user_input in {"buy", "fill", "take", "remaining", "exit"}:
                iterator_local_var = False
            else:
                iterator_local_var = True
            return iterator_local_var

        user_input = ""
        while iterator_var:
            user_input = input("Write action (buy, fill, take, remaining, exit):\n> ")
            user_input = CoffeeMachineData.my_replace(user_input)
            iterator_var = check_input()
        return user_input

    def user_take(self):
        """Take money from coffee machine func, ничего не возвращает"""
        print(f"I gave you {CoffeeMachineData.money}")
        CoffeeMachineData.money = 0

    def user_fill(self):
        """Fill coffee machine func, ничего не возвращает"""
        iterator_var = True
        while iterator_var:
            water_count = input("Write how many ml of water do you want to add:\n> ")
            milk_count = input("Write how many ml of milk do you want to add:\n> ")
            coffee_beans_count = input("Write how many grams of coffee beans do you want to add:\n> ")
            cups_count = input("Write how many disposable cups of coffee do you want to add:\n> ")
            print("\n")

            try:
                CoffeeMachineData.water += int(water_count)
                CoffeeMachineData.milk += int(milk_count)
                CoffeeMachineData.coffee_beans += int(coffee_beans_count)
                CoffeeMachineData.cup += int(cups_count)
            except ValueError:
                print("You should enter numbers!")
                iterator_var = True
            else:
                iterator_var = False

    def user_buy(self):
        """Buy coffee func, ничего не возвращает"""
        iterator_var = True
        while iterator_var:
            number_coffee = input(WHAT_DO_YOU_WANT)
            if number_coffee == "1":
                iterator_var = False
                current_coffee = ESPRESSO
            elif number_coffee == "2":
                iterator_var = False
                current_coffee = LATTE
            elif number_coffee == "3":
                iterator_var = False
                current_coffee = CAPPUCCINO
            elif number_coffee == "back":
                iterator_var = False
                return
            else:
                iterator_var = True
        self.buy_coffee(current_coffee)

    def buy_coffee(self, coffee):
        """Buy coffee func, ничего не возвращает, coffee - объект класса coffee, текущий кофе, который покупаем"""
        if coffee.water > CoffeeMachineData.water:
            print("Sorry, not enough water!")
        elif coffee.milk > CoffeeMachineData.milk:
            print("Sorry, not enough milk!")
        elif coffee.coffee_beans > CoffeeMachineData.coffee_beans:
            print("Sorry, not enough beans!")
        else:
            CoffeeMachineData.water -= coffee.water
            CoffeeMachineData.coffee_beans -= coffee.coffee_beans
            CoffeeMachineData.milk -= coffee.milk
            CoffeeMachineData.cup -= 1
            CoffeeMachineData.money += coffee.price
            print(MAKE_COFFEE)


def lobby():
    """Start func"""
    game_play()


def game_play():
    """Main func"""
    machine = CoffeeMachine()
    user_play = True
    while user_play:
        user_input = machine.my_input()
        user_play = machine.check_user_input(user_input)


# Точка входа
if __name__ == "__main__":
    lobby()
    