"""Calculator module"""
import math

# a - ежемесячный платеж, p - основная сумма кредита, i - месячная процентная ставка,
# n - количество платежей """


class AnnualCalc:
    """main annual loan class"""
    @staticmethod
    def calculate_periods(p, a, i) -> int:
        """p-основная сумма кредита, a-ежемесячный платеж, i-годовая процентная ставка"""
        if i == 0:
            n = p/a
        else:
            i = i/1200
            number = a/(a - i * p)
            n = math.log(number, 1+i)
        return math.ceil(n)

    @staticmethod
    def calculate_monthly_payments(p, n, i) -> int:
        """Рассчитать ежемесячный платеж, p-основная сумма кредита, n-количество месяцев
        i-годовая процентная ставка"""
        if i == 0:
            a = p/n
        else:
            i = i/1200
            a = p * ((i * ((1+i)**n))/(((1+i)**n) - 1))
        return math.ceil(a)

    @staticmethod
    def calculate_loan_principal(a, n, i) -> int:
        """Рассчитать общую сумму кредита, a-ежемесячная плата, n-количество месяцев,
        i-годовая процентная ставка"""
        i = i/1200
        p = a/((i*((1+i)**n)) / (((1+i)**n)-1))
        return math.floor(p)


class DifferentialCalc:
    """Main diff class"""
    @staticmethod
    def calculate_monthly_payments(p, n, i) -> int:
        """Рассчитать плату для каждого месяца, p-основная сумма кредита, n-количество месяцев
        i-годовая процентная ставка, m-номер месяца, за который указали месячную плату"""
        i = i/1200
        monthly_payments = []
        for m in range(1, n + 1):
            d = (p / n) + (i * (p - ((p * (m - 1)) / n)))
            monthly_payments.append(math.ceil(d))
        return monthly_payments

    @staticmethod
    def calculate_loan_principal(n, i, d, m) -> int:
        """Рассчитать общую сумму кредита, n-количество месяцев, i-годовая процентная ставка,
        d-плата m-ный месяц, m-номер месяца"""
        p = (d * 1200 * n) / (1200 + i*n - i*(m-1))
        return int(p)

    @staticmethod
    def calculate_periods(p, i, d, m) -> int:
        """Рассчитать количество платежей, p-общая сумма кредита
        i-процентная годовая ставка, d-плата за m-ный месяц, m-номер месяца"""
        i = i/1200
        n = (p-(i*p*(m-1)))/(d-i*p)
        return round(n)


differential_calc = DifferentialCalc()
annual_calc = AnnualCalc()
