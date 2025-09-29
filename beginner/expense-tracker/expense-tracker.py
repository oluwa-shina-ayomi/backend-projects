import argparse
import csv
from datetime import datetime
from tabulate import tabulate

expenses = []
def main():
    global expenses
    load_file()

    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="to take any action(add, list, summary or delete)")
    parser.add_argument("-m","--month", help="specify summary of month", type=int)
    parser.add_argument("-d", "--description", help="expense")
    parser.add_argument("-a","--amount", help="cost of expense", type=int)
    parser.add_argument("-i","--id", help="unique number for an expense", type=int)
    args = parser.parse_args()

    mode = args.mode
    if mode == "add":
        description = args.description
        amount = args.amount
        date = datetime.now().strftime("%Y-%m-%d")
        id = generate_id()
        expenses.append({
            "id": int(id), 
            "date": date, 
            "description": description, 
            "amount": amount
        })
        save_file()
        print(f"Expense added successfully (ID: {id})")
    elif  mode == "list":
        table = []
        for expense in expenses:
            print(f"ID: {expense["id"]}, Date: {expense["date"]}, Description: {expense["description"]}, Amount: {expense["amount"]}")

    elif mode == "summary":
        month = args.month
        total_amount = 0
        if not month:
            for expense in expenses:
                total_amount += float(expense["amount"])
        for expense in expenses:
            date = expense["date"]
            y, m, d = date.split("-")
            if int(m) == int(month):
                total_amount += float(expense["amount"])
        print(f"Total expenses: ${total_amount}")

    elif mode == "delete":
        id = int(args.id)
        deleted = False
        for i, expense in enumerate(expenses):
            if id == expense["id"]:
                del expenses[i]
                deleted = True
                break
        if deleted:
            for idx, expense in enumerate(expenses, start=1):
                expense["id"] = idx
        if not deleted:
                print("Expense not made yet")
        save_file()
        print("Expense deleted successfully")
    else:
        print("run 'python expense-tracker.py -h' to learn how to use")

def load_file():
    global expenses
    try:
        with open("expenses.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "id": int(row["id"]),
                    "date": row["date"],
                    "description": row["description"],
                    "amount": row["amount"]
                })
    except FileNotFoundError:
        expenses = []
    except Exception:
        expenses = []

def save_file():
    global expenses
    with open("expenses.csv","w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "date", "description", "amount"])
        writer.writeheader()
        writer.writerows(expenses)

def generate_id():
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1

if __name__ == "__main__":
    main()