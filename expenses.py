import csv  # Import for CSV handling
import json  # Import for JSON handling
from datetime import datetime  # Import for date handling

# Load existing expenses from a JSON file
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)  # Load data into the expenses list
    print(f"You have {len(expenses)} expenses logged.")
except FileNotFoundError:
    expenses = []  # Initialize as an empty list if the file doesn't exist
    print("No existing expense data found. Starting fresh.")

# Function to save expenses when the program ends

def save_expenses():
    print("Attempting to save expenses...")
    
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)
        print("Expenses saved successfully!")
    except Exception as e:
        print(f"Error saving expenses: {e}")



# Main program and other functions...
def add_expense():
    print("\n--- Add a New Expense ---")
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category (e.g., food, travel): ")
        date = input("Enter the date (YYYY-MM-DD): ")
        datetime.strptime(date, '%Y-%m-%d')  # Validate date format

        # Add the expense to the list
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

def view_monthly_summary():
    print("\n--- View Monthly Summary ---")
    try:
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year (e.g., 2024): "))

        # Filter expenses by month and year
        filtered_expenses = [
            e for e in expenses
            if datetime.strptime(e['date'], '%Y-%m-%d').month == month
            and datetime.strptime(e['date'], '%Y-%m-%d').year == year
        ]

        # Display summary
        if not filtered_expenses:
            print("No expenses found for this period.")
        else:
            print("\nExpenses for {}/{}:".format(month, year))
            for expense in filtered_expenses:
                print(f"- {expense['date']}: {expense['category']} - ${expense['amount']:.2f}")

            total = sum(e['amount'] for e in filtered_expenses)
            print(f"Total: ${total:.2f}")
    except ValueError:
        print("Invalid input. Please try again.")

def export_to_csv():
    print("\n--- Export to CSV ---")
    filename = input("Enter the filename (e.g., expenses.csv): ")
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expenses exported successfully to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add an Expense")
        print("2. View Monthly Summary")
        print("3. Export to CSV")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_summary()
        elif choice == '3':
            export_to_csv()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    try:
        main()  # Run the main function
    finally:
        save_expenses()  # Save expenses before the program ends
