from storage import load_expenses

from utils import (
    add_expenses,
    view_expenses,
    view_total,
    view_by_category,
    delete_expenses,
    edit_expenses,
    export_to_csv
)
    
def main():
    expenses = load_expenses()
    while True:
        print("\n===Expense Tracker===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. View Total")
        print("4. View Expenses By Category")
        print("5. Edit Expense")
        print("6. Delete Expense")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            view_by_category(expenses)
        elif choice == "5":
            edit_expenses(expenses)
        elif choice == "6":
            delete_expenses(expenses)
        elif choice == "7":
            export_to_csv(expenses)
        elif choice == "8":
            print("Goodbye")
            break
        else:
            print("invalid choice, try again")

main()