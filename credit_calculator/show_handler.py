"""Show handler module"""


class ShowHandler:
    """Show handler class"""
    @staticmethod
    def over_payment(principal, payments: list) -> int:
        """Рассчитать переплату, p-общая сумма кредита, a-ежемесячный платеж,
        n-количество месяцев, если diff loan, то n=0, a - список со всеми платами"""
        over_payment = 0
        for index in payments:
            over_payment += index
        over_payment = round(over_payment - principal)
        print(f"Overpayment = {over_payment}")

    @staticmethod
    def show_monthly_payment(monthly_payments) -> None:
        """monthly_payments - список всех платажей по месяцам, p-общая сумма кредита,
        n-количество месяцев"""
        if len(monthly_payments) > 1:
            index = 1
            for j in monthly_payments:
                print(f"Month {index}: payment is {j}")
                index += 1
        else:
            print(f"Your monthly payment = {monthly_payments[0]}!")

    @staticmethod
    def show_periods(periods_number) -> str:
        """Отобразить количество месяцев, лет для выплаты кредита,
        periods_number-количество месяцев"""
        periods_years = periods_number // 12
        periods_months = periods_number % 12
        text = "It will take "
        if periods_years != 0:
            text += f"{periods_years} years "
        elif periods_years != 0 and periods_months != 0:
            text += "and "
        if periods_months != 0:
            text += f"{periods_months} months "
        text += "to repay this loan!"
        print(text)


show_handler = ShowHandler()
