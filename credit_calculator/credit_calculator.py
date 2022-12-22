"""main script"""
from noparser_handler import noparser_handler
from parser_handler import parser_handler


class Credits:
    """Main Credits class"""
    def __init__(self):
        self.TYPE_OF_LOAN = """Enter a type of loan:
    a - annual
    d - differential
    exit - to quit """

    @staticmethod
    def check_user_choice(user_choice) -> bool:
        """Проверить корректность запроса пользователя, возвращает bool"""
        if user_choice.lower() in {"a", "p", "n"}:
            return False
        print("Incorrect format!")
        return True


def main() -> None:
    """Main func"""
    while True:
        print(credits.TYPE_OF_LOAN)
        type_of_loan = input("> ")
        match type_of_loan.lower():
            case "a":
                noparser_handler.annual_handler()
                break
            case "d":
                noparser_handler.differential_handler()
                break
            case "exit":
                return


def lobby():
    """Lobby func"""
    print("Credit Calculator by Maks!")
    parser_correct = parser_handler.check_parser_correct()
    match parser_correct:
        case "parser":
            parser_handler.parser_handler()
        case "exit":
            return
        case "noparser":
            main()


# Точка входа
if __name__ == "__main__":
    credits = Credits()
    lobby()
