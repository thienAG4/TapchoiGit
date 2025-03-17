import json

class Element:
    def __init__(self, expenses, incomes):
        self.expenses = expenses
        self.incomes = incomes
    def total_incomes(self):
        with open(self.incomes) as f:
            incomes_list = json.load(f)
        total_income = abs(sum(incomes_list["amout"].values()))
        return total_income
    def total_expenses(self):
        with open(self.expenses) as f:
            expenses_list = json.load(f)
        total_expense = abs(sum(expenses_list["amout"].values()))
        return total_expense

