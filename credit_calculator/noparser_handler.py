"""NoParser mode start handler module"""
from calculator import annual_calc
from calculator import differential_calc
from show_handler import show_handler


class NoParserHandler:
    """NoParser mode handler"""
    def __init__(self):
        self.WHAT_DO_WANT = """What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:"""

        self.MONTHLY_PAYMENT = """Enter the monthly payments: > """

        self.ERROR_DIFF = "In the Differential Loan can calculating only monthly payment!"

        self.NO_CORRECT_FORMAT = "No correct format!"

        self.principal = 0

        self.monthly_payment = 0

        self.monthly_payments = []

        self.periods = 0

        self.interest = 0

    def input_arguments_for_annual(self, user_choice) -> None:
        """Функция инпута данных от пользователя для ежегодного кредита"""
        match user_choice:
            case "a":
                self.input_p()
                self.input_n()
                self.input_i()
            case "p":
                self.input_a()
                self.input_n()
                self.input_i()
            case "n":
                self.input_p()
                self.input_a()
                self.input_i()

    def input_p(self) -> None:
        """Loan Principal input func"""
        iterator = True
        while iterator:
            p = input("Enter the principal_loan: > ")
            try:
                p = int(p)
                if p > 0:
                    iterator = False
                    self.principal = p
            except ValueError:
                print(self.NO_CORRECT_FORMAT)

    def input_a(self) -> None:
        """Monthly Payment input func"""
        iterator = True
        while iterator:
            a = input("Enter an annuity payment: > ")
            try:
                a = float(a)
                if a <= 0:
                    print("Monthly payment must be more than 0!")
                else:
                    iterator = False
                    self.monthly_payment = a
            except ValueError:
                print(self.NO_CORRECT_FORMAT)

    def input_n(self) -> None:
        """Periods of credit input func"""
        iterator = True
        while iterator:
            n = input("Enter the number of periods: > ")
            try:
                n = int(n)
                if n <= 0:
                    print("Number of periods must be more than 0!")
                else:
                    iterator = False
                    self.periods = n
            except ValueError:
                print(self.NO_CORRECT_FORMAT)

    def input_i(self) -> None:
        """Interest of credit input func"""
        iterator = True
        while iterator:
            i = input("Enter an interest: > ")
            try:
                i = float(i)
                if i < 0:
                    print("Interest cannot be a negative number!")
                else:
                    iterator = False
                    self.interest = i
            except ValueError:
                print(self.NO_CORRECT_FORMAT)

    def annual_handler(self) -> None:
        """Annual loan handler"""
        while True:
            print(self.WHAT_DO_WANT)
            user_choice = input("> ")
            if user_choice not in {"a", "p", "n"}:
                print(self.NO_CORRECT_FORMAT)
            else:
                break
        self.input_arguments_for_annual(user_choice)
        match user_choice:
            case "a":
                monthly_payment = annual_calc.calculate_monthly_payments(self.principal, self.periods, self.interest)
                self.monthly_payment = monthly_payment
                show_handler.show_monthly_payment([monthly_payment])
            case "p":
                principal = annual_calc.calculate_loan_principal(self.monthly_payment, self.periods, self.interest)
                self.principal = principal
                print(f"Your principal of loan = {principal}")
            case "n":
                periods = annual_calc.calculate_periods(self.principal, self.monthly_payment, self.interest)
                self.periods = periods
                show_handler.show_periods(periods)
        for _ in range(self.periods):
            self.monthly_payments.append(self.monthly_payment)
        show_handler.over_payment(self.principal, self.monthly_payments)

    def differential_handler(self) -> None:
        """Differential loan handler"""
        self.input_p()
        self.input_n()
        self.input_i()
        a = differential_calc.calculate_monthly_payments(self.principal, self.periods, self.interest)
        self.monthly_payments = a
        show_handler.show_monthly_payment(a)
        show_handler.over_payment(self.principal, self.monthly_payments)


noparser_handler = NoParserHandler()
