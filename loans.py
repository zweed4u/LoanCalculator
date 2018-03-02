#!/usr/bin/python3


class Loan:
    def __init__(self, loan_amount, years_to_pay_off, interest,
                 initial_payment=None):
        self.amount_loaned = loan_amount
        if initial_payment:
            self.amount_loaned -= initial_payment
        self.years = years_to_pay_off
        self.interest = interest

    def calulcate(self):
        number_of_payments = self.years * 12  # total payments
        annual_interest = (self.interest / 100) / 12
        discount_factor = (((1 + annual_interest) ** number_of_payments) - 1) / (
                          annual_interest * ((1 + annual_interest) ** number_of_payments))
        print(f'{self.amount_loaned} at {self.interest}% for {self.years} years')
        print(f'{self.amount_loaned / discount_factor} per month for {self.years} years')


# $100,000 borrowd at 6% for 30 years repayment
Loan(100000, 30, 6).calulcate()