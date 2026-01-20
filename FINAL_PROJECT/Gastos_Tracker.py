expenses = []
funds = 0.0


def add_expense():
    global funds
    description = input("Enter expense description (e.g., 'Grocery'): ")
    amount = float(input("Enter amount (PHP): "))

    if amount > funds:
        print(f" Insufficient funds! Need PHP {amount:.2f}, have PHP {funds:.2f}")
        return
    funds -= amount
    expenses.append({"description": description, "amount": amount, })
    print(f" Expense added & deducted! Remaining: PHP {funds:.2f}")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    total = 0
    for exp in expenses:
        print(f"{exp['description']}: PHP {exp['amount']:.2f} ")
        total += exp['amount']
    print(f"Total spent: PHP {total:.2f}")


def fund_function():
    global funds
    print(f"\nCurrent funds: PHP {funds:.2f}")
    action = input("Add (a) or deduct (d) funds? Enter 'a' or 'd': ")

    if action.lower() == 'a':
        add_amount = float(input("Enter amount to add: "))
        funds += add_amount
        print(f"Added PHP {add_amount:.2f}. New balance: PHP {funds:.2f}")
    elif action.lower() == 'd':
        deduct_amount = float(input("Enter amount to deduct: "))
        if deduct_amount <= funds:
            funds -= deduct_amount
            print(f"Deducted PHP {deduct_amount:.2f}. New balance: PHP {funds:.2f}")
        else:
            print(" Insufficient funds!")
    else:
        print("Invalid choice!")


def reset_all():
    global expenses, funds
    expenses = []
    funds = 0.0
    print(" ALL DATA RESET! Expenses cleared. Funds reset to PHP 0.00")
    print("Start fresh!")


# Main loop
while True:
    print("\n=== Gastos Tracker (COMPLETE) ===")
    print("1. Add expense ")
    print("2. View expenses")
    print("3. Manage funds")
    print("4.  RESET ALL DATA")
    print(f" Funds: PHP {funds:.2f}")
    choice = input("Choose (1/2/3/4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        fund_function()
    elif choice == '4':
        reset_all()
    else:
        print("Invalid. Choose 1, 2, 3, or 4.")