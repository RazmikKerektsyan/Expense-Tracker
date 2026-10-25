#my first project with python
# it is Expense Tracker

import json
from tabulate import tabulate

import sys

try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)

except FileNotFoundError:
    expenses = []

except json.JSONDecodeError:
    print("Error: expenses.json is corrupted!")
    print("Your data has not been changed.")
    sys.exit(1)

def save_expenses():
    with open("expenses.json", "w", encoding="utf-8") as json_file:
        json.dump(expenses, json_file, indent=4, ensure_ascii=False)


while True:

    print("=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View total expenses")
    print("3. Show expenses")
    print("4. Show expenses by category")
    print("5. Delete expense")
    print("6. Exit")


    try:
        select = int(input("Select an option: (1-6) "))
        if select == 1:
            print("1. Add expense")
        elif select == 2:
            print("2. View total expenses")
        elif select == 3:
            print("3. Show expenses")
        elif select == 4:
            print("4. Show expenses by category")
        elif select == 5:
            print("5. Delete expense")
        elif select == 6:
            print("6. Exit")
            break
        else:
            print("Invalid option")
    except ValueError:
        print("Invalid option")
        continue


    if select == 1:
        name = input("Enter expense name: ").strip()
        if not name.strip():
            print("Invalid expense name!")
        else:
            try:
                amount = float(input("Enter expense price: "))
                if amount <= 0:
                    print("Invalid price!")
                else:
                    category = input("Enter expense category: ").strip()
                    if not category.strip():
                        print("Invalid expense category!")
                    else:
                        expense = {
                            "name": name,
                            "amount": amount,
                            "category": category
                        }
                        expenses.append(expense)
                        save_expenses()
                        print("Expense added successfully!")
            except ValueError:
                print("Invalid price!")



    elif select == 2:
        if not expenses:
            print("There are no expenses added!")
        else:
            total = 0
            for expense in expenses:
                total += expense["amount"]
            print("Total spent:", total, "GEL")

    elif select == 3:
        if not expenses:
            print("No expenses added!")
        else:
            print("Expenses added:")
            print(tabulate(expenses, headers="keys", tablefmt="grid"))


    elif select == 4:

        category = input("Enter expense category: ").strip()
        category_expenses = []

        for expense in expenses:
             if category == expense["category"]:
                category_expenses.append(expense)
        if not category_expenses:
            print("There are no expenses in this category!")
        else:
            print(tabulate(category_expenses, headers="keys", tablefmt="grid"))

    elif select == 5:
        if not expenses:
            print("No expenses added!")
        else:
            print((tabulate(expenses, headers="keys", tablefmt="grid")))
            try:
                number = int(input("Enter number for deleting expense: "))
                if 1 <= number <= len(expenses):
                    index = number - 1
                    expenses.pop(index)
                    save_expenses()
                    print("Expense deleted successfully!")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Invalid number!")