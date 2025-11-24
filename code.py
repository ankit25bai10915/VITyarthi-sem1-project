# Where Is My Money Going? - Python Expense Tracker

expenses = []  # List to store all expenses


def add_expense():
    try:
        amount = float(input("Enter amount spent: ₹ "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input(
        "Enter category (Food, Travel, Shopping, Bills, Entertainment, etc.): ")
    note = input("Optional note/description: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_all_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} ({exp['note']})")
    print()


def view_total_spent():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    total = sum(exp["amount"] for exp in expenses)

    # Calculate category spending
    category_totals = {}
    for exp in expenses:
        category = exp["category"]
        category_totals[category] = category_totals.get(
            category, 0) + exp["amount"]

    # Find top category
    top_category = max(category_totals, key=category_totals.get)

    print(f"\nYour total expense today is: ₹{total}")
    print(f"You spent the most on: {top_category}\n")


def main_menu():
    while True:
        print("--- Where Is My Money Going? ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_total_spent()
        elif choice == "4":
            print("Goodbye! Stay mindful of your spending ✨")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")


# Start the program
main_menu()
