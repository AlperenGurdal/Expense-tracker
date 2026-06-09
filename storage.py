import json

FILE_NAME = "expenses.json"
INCOME_FILE = "income.json"


def load_expenses():
    with open( FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent =4)

def load_income():
    with open(INCOME_FILE, "r") as file:
        return json.load(file)

def save_income(income):
    with open(INCOME_FILE, "w") as file:
        json.dump(income, file, indent=4)