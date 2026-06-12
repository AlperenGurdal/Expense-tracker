import csv
from storage import (
    save_expenses,
    save_income
)

def add_expenses(expenses):
    description = input("description: ")
    try:
        amount = float(input("amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    category = input("category: ")

    expenses.append({"description": description,
        "amount": amount, "category": category})
    
    save_expenses(expenses)
    print("Expense Added!")

def view_expenses(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    print("\n === Expenses ===")
    
    for i, expense in enumerate(expenses, start=1):
        category = expense.get("category", "No Category")

        print(
            f"{i}. {expense['description']} "
            f"({category}) - "
            f"${expense['amount']:.2f}")

def view_total(expenses):
    if not expenses:
        print("no expenses yet")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spent: ${total:.2f}")

def delete_expenses(expenses):#gonna be editted
    if not expenses:
        print("no expense to delete")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("Enter expense number to delete: "))
        index = index -1
    except ValueError:
        print("invalid input")
        return
    
    if  0 <= index < len(expenses):
        removed = expenses.pop(index)

        save_expenses(expenses)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")

def view_by_category(expenses):#gonna be editted
    if not expenses:
        print("No expenses yet.")
        return
    category_totals = {}
    total_spent = 0

    for expense in expenses:
        category = expense.get("category","No Category")
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        total_spent += amount


    print("\n=== Spending by Category ===")

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")  
    
    print("\n----------------------")
    print(f"TOTAL: ${total_spent:.2f}")

def edit_expenses(expenses):#gonna be editted
    

    if not expenses:
        print("no expenses to edit")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("Enter Expense number to edit: "))-1
    except ValueError:
        print("invalid input")
        return
    
    if not (0 <= index < len(expenses)):
        print("Invalid expense number.")
        return
    
    expense = expenses[index]
    print("\nLeave blank to keep current value.")

    description = input(f"Description [{expense['description']}]: ")
    amount_input = input(f"Amount [{expense['amount']}]: ")
    category = input(f"Category [{expense['category']}]: ")
    
    if description:
        expense["description"] = description

    if amount_input:
        try:
            expense["amount"] = float(amount_input)
        except ValueError:
            print("Invalid amount.")
            return

    if category:
        expense["category"] = category
    
    save_expenses(expenses)
    print("Expense updated!")

def export_to_csv(expenses):#gonna be editted
    if not expenses:
        print("No expenses to export")
        return
    
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Description", "Amount", "Category"])
    
        for expense in expenses:
            writer.writerow([expense["description"], expense["amount"], expense.get("category", "No Category")])
    
    print("Expenses are now exported to expenses.csv")

    #######################INCOME###################################

def add_income(income):
    description = input("description: ")
    try:
        amount = float(input("amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    category = input("category: ")

    income.append({ "type": "income", "description": description,"amount": amount, "category": category})
    
    save_income(income)
    print("Income Added!")        

def view_income(income):
    if not income:
        print("no income yet")
        return
    
    print("\n === Income ===")
    
    for i, entry in enumerate(income, start=1):
        category = entry.get("category", "No Category")

        print(f"{i}. {entry['description']} "f"({category}) - "f"${entry['amount']:.2f}")
            
def view_income_total(income):
    total = sum(item["amount"] for item in income)

    print(f"Total Income: ${total:.2f}")

def edit_income(income):
    if not income:
        print("no income to edit")
        return

    view_income(income)

    try:
        index = int(input("Enter income number to edit: ")) - 1
    except ValueError:
        print("invalid input")
        return

    if not (0 <= index < len(income)):
        print("Invalid income number.")
        return

    entry = income[index]
    print("\nLeave blank to keep current value.")

    description = input(f"Description [{entry['description']}]: ")
    amount_input = input(f"Amount [{entry['amount']}]: ")
    category = input(f"Category [{entry['category']}]: ")

    if description:
        entry["description"] = description

    if amount_input:
        try:
            entry["amount"] = float(amount_input)
        except ValueError:
            print("Invalid amount.")
            return

    if category:
        entry["category"] = category

    save_income(income)
    print("Income updated!")

def view_income_by_category(income):#gonna be editted
    if not income:
        print("No income yet.")
        return
    category_totals = {}
    total_spent = 0

    for entry in income:
        category = entry.get("category","No Category")
        amount = entry["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        total_spent += amount


    print("\n=== Income by Category ===")

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")  
    
    print("\n----------------------")
    print(f"TOTAL: ${total_spent:.2f}")

def delete_income(income):#gonna be editted
    if not income:
        print("no income to delete")
        return
    
    view_income(income)
    
    try:
        index = int(input("Enter income number to delete: "))
        index = index -1
    except ValueError:
        print("invalid input")
        return
    
    if  0 <= index < len(income):
        removed = income.pop(index)

        save_income(income)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")
    
def view_balance(expenses, income):
    total_expenses = sum(expense["amount"]for expense in expenses)

    total_income = sum(item["amount"]for item in income)

    balance = total_income - total_expenses

    print("\n=== Financial Summary ===")
    print(f"Income:   ${total_income:.2f}")
    print(f"Expenses: ${total_expenses:.2f}")
    print("----------------------")
    print(f"Balance:  ${balance:.2f}")

def view_net_by_category(expenses, income):
    net_categories = {}

    # Add expenses (negative impact)
    for e in expenses:
        category = e.get("category", "No Category")
        amount = -e["amount"]

        if category in net_categories:
            net_categories[category] += amount
        else:
            net_categories[category] = amount

    # Add income (positive impact)
    for i in income:
        category = i.get("category", "No Category")
        amount = i["amount"]

        if category in net_categories:
            net_categories[category] += amount
        else:
            net_categories[category] = amount

    print("\n=== Net Category Summary ===")

    for category, total in net_categories.items():
        sign = "+" if total >= 0 else "-"
        print(f"{category}: {sign}${abs(total):.2f}")

def monthly_summary(expenses, income):
    total_expenses = sum(e["amount"] for e in expenses)
    total_income = sum(i["amount"] for i in income)

    net = total_income - total_expenses

    print("\n=== Monthly Summary ===")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("----------------------")
    print(f"Net Balance:    ${net:.2f}")

    if net > 0:
        print("Status: Positive month 👍")
    elif net < 0:
        print("Status: Negative month ⚠️")
    else:
        print("Status: Break-even")