import json

FILE_NAME = "expenses.json"

def load_expenses():
    with open( FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent =4)