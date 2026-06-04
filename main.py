import json

FILE_NAME = "expenses.json"

def load_expenses():
    with open( FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent =4) 


def add_expenses(expenses):
    description = input("description: ")
    try:
        amount = float(input("amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expenses.append({"description": description,
        "amount": amount})
    
    save_expenses(expenses)
    print("Expense Added!")

def view_expenses(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    print("\n === Expenses ===")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f}")

def view_total(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ${total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n===Expense Tracker===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Total")
        print("4. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("invalid choice, try again")

main()