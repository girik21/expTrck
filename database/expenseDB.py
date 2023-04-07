import sys
sys.path.append('./')
from components.expense import Expense
import csv

class ExpenseRepository:
    def __init__(self, filename:str = "./csv/expense.csv") -> None:
        self.__filename = filename
        
    #read epense data from csv file
    def read_expenses(self) -> list[Expense]:
        expenses : list[Expense] = []
    
        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
            
            for row in reader:
                if len(row) == 4:
                   expense = Expense(int(row[0]), row[1], int(row[2]), row[3])
                   expenses.append(expense)
                else:
                   print(f"Skipping row {row} because it doesn't have the expected number of columns.")

        return expenses
    
    #write employee data
    def write_expenses(self, expenses: list[Expense]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for expense in expenses:
                writer.writerow(expense.get_csv())

def main():
    #Try for Expense Data
    exp_db = ExpenseRepository()
    
    #test for reading expense from repo
    expenses = exp_db.read_expenses()
    for expense in expenses:
        print("\n")
        print(expense)
    
    expense = Expense(1, "2000-01-01", 700, "old")
    expenses.append(expense)
    print("\n")
    exp_db.write_expenses(expenses)

if __name__ == "__main__":
    main()