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
    edit_income,
    delete_income,
    view_income_by_category,
    view_balance,
    view_net_by_category,
    monthly_summary
)
    
def main():
    expenses = load_expenses()
    income = load_income()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. View Income")
        print("5. View Expense Total")
        print("6. View Income Total")
        print("7. View Expense Categories")
        print("8. View Income Categories")
        print("9. View Balance")
        print("10. View Net By Category")
        print("11. Monthly Summary")
        print("12. Edit Expense")
        print("13. Delete Expense")
        print("14. Edit Income")
        print("15. Delete Income")
        print("16. Export to CSV")
        print("17. Exit")

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
            view_income_by_category(income)

        elif choice == "9":
            view_balance(expenses, income)

        elif choice == "10":
            view_net_by_category(expenses, income)

        elif choice == "11":
            monthly_summary(expenses, income)

        elif choice == "12":
            edit_expenses(expenses)

        elif choice == "13":
            delete_expenses(expenses)

        elif choice == "14":
            edit_income(income)

        elif choice == "15":
            delete_income(income)

        elif choice == "16":
            export_to_csv(expenses)

        elif choice == "17":
            print("Goodbye")
            break

        else:
            print("Invalid choice, try again")

main()  