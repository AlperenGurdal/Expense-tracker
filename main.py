from storage import (
    load_expenses,
    load_income
)

from utils import (
    add_expenses,
    view_expenses,
    view_total,
    view_by_category,
    delete_expenses,
    edit_expenses,
    export_to_csv,
    add_income,
    view_income,
    view_income_total,
    view_balance
)
    
def main():
    expenses = load_expenses()
    income = load_income()
    while True:
        print("\n===Expense Tracker===")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expense")
        print("4. view Income")
        print("5. View Expense Total")
        print("6. View Income Total")
        print("7. View By Category")
        print("8. View Balance")
        print("9. Edit Expense")
        print("10. Delete Expense")
        print("11. Export to CSV")
        print("12. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            add_income(income)
        elif choice == "3":
            view_expenses(expenses)
        elif choice == "4":
            view_income(income)
        elif choice == "5":
            view_total(expenses)
        elif choice == "6":
            view_income_total(income)
        elif choice == "7":
            view_by_category(expenses)
        elif choice == "8":
            view_balance(expenses, income)
        elif choice == "9":
            edit_expenses(expenses)
        elif choice == "10":
            delete_expenses(expenses)
        elif choice == "11":
            export_to_csv(expenses)
        elif choice == "12":
            print("Goodbye")
            break
        else:
            print("invalid choice, try again")

main()  