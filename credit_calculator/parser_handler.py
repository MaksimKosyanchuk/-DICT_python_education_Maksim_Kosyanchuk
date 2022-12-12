"""Parser mode start handler module"""
import sys
import argparse
from calculator import annual_calc
from calculator import differential_calc
from show_handler import show_handler


class ParserHandler:
    """Class for parser-mode"""
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-t', '--type', default='none')
        self.parser.add_argument('--principal', default='none')
        self.parser.add_argument('--payment', default='none')
        self.parser.add_argument('--periods', default='none')
        self.parser.add_argument('--interest', default='none')
        self.unknown_value = ""
        self.namespace = self.parser.parse_args(sys.argv[1:])

    def check_parser_correct(self) -> str:
        """ "exit" - если надо неверные параметры, и закрыть программу,
         "parser" - если аргументы верны, "noparser" - если нет аргументов"""
        # количество отсутствующих параметров
        missing_value = 0
        if self.namespace.type != "none":
            if self.namespace.type not in {"diff", "annuity"}:
                print("Incorrect type loan!")
                return "exit"
        else:
            missing_value += 1
            self.unknown_value = "type"
        if self.namespace.principal != "none":
            try:
                self.namespace.principal = int(self.namespace.principal)
                if self.namespace.principal <= 0:
                    print("Loan principal should be more than 0!")
                    return "exit"
            except ValueError:
                print("ValueError: loan_principal must be integer!")
                return "exit"
        else:
            missing_value += 1
            self.unknown_value = "principal"
        if self.namespace.periods != "none":
            try:
                self.namespace.periods = int(self.namespace.periods)
                if self.namespace.periods <= 0:
                    print("ValueError: periods must be more than 0!")
            except ValueError:
                print("ValueError: periods must be integer!")
                return "exit"
        else:
            missing_value += 1
            self.unknown_value = "periods"
        if self.namespace.payment != "none":
            if self.namespace.type == "annuity":
                try:
                    self.namespace.payment = float(self.namespace.payment)
                    if self.namespace.payment <= 0:
                        print("ValueError: payment must be more than 0!")
                        return "exit"
                except ValueError:
                    print("ValueError: payment must be float!")
                    return "exit"
            elif self.namespace.type == "diff":
                print("Impossible to specify payment for the differential loan!")
                return "exit"
        else:
            missing_value += 1
            self.unknown_value = "payment"
        if self.namespace.interest != "none":
            try:
                self.namespace.interest = float(self.namespace.interest)
                if self.namespace.interest < 0:
                    print("ValueError: interest must be at least 0!")
                    return "exit"
            except ValueError:
                print("ValueError: interest must be a float!")
                return "exit"
        else:
            missing_value += 1
            self.unknown_value = "interest"
        if missing_value == 1:
            if self.namespace.type == "diff" and self.unknown_value != "payment":
                print("In the differential loan could be calculate only monthly payments!")
                return "exit"

            if self.unknown_value in {"interest", "type"}:
                print("Incorrect format!")
                return "exit"
            return "parser"
        if missing_value == 5:
            return "noparser"
        print("Enter the 4 parameters!")
        return "exit"

    def parser_handler(self) -> None:
        """Основной обработчик parser-mode запуска"""
        match self.namespace.type:
            case "diff":
                monthly_payments = differential_calc.calculate_monthly_payments(self.namespace.principal, self.namespace.periods, self.namespace.interest)
                show_handler.show_monthly_payment(monthly_payments)
                show_handler.over_payment(self.namespace.principal, monthly_payments)
            case "annuity":
                match self.unknown_value:
                    case "principal":
                        self.namespace.principal = annual_calc.calculate_loan_principal(self.namespace.payment, self.namespace.periods, self.namespace.interest)
                        print(f"Your loan principal = {self.namespace.principal}")
                    case "payment":
                        self.namespace.payment = annual_calc.calculate_monthly_payments(self.namespace.principal, self.namespace.periods, self.namespace.interest)
                        show_handler.show_monthly_payment([self.namespace.payment])
                    case "periods":
                        self.namespace.periods = annual_calc.calculate_periods(self.namespace.principal, self.namespace.payment, self.namespace.interest)
                        show_handler.show_periods(self.namespace.periods)
                payments = []
                for _ in range(self.namespace.periods):
                    payments.append(self.namespace.payment)
                show_handler.over_payment(self.namespace.principal, payments)


parser_handler = ParserHandler()
