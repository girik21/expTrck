import sys
sys.path.append('./')
from components.employee import Employee
from components.expense import Expense
from components.department import Department
from components.departmentManager import DepartmentManager

class ExpenseTracker:
    def __init__(self) -> None:
        self.__department = Department("CSE")
        self.__departmentManager = DepartmentManager()
    
    def show_menu(self):
        print()
        print("Menu")
        print("1. Add an Employee")
        print("2. Print list of Employees")
        print("3. Search Employees by EmpId")
        print("4. Remove Employee")
        print("5. Edit Employee")
        print("6. Add Expense")
        print("7. Show all Expenses")
        print("8. Remove Expenses")
        print("9. Edit Expense")
        print("10. Show all Department")
        print("11. Add Department")
        print("12. Update Department")
        print("13. Delete Department")

        print("0. Exit")
    
    #Get user input
    def get_user_choice(self) -> int:
        choice = int(input("Enter your choice: "))
        return choice
    
    def process_command(self, choice: int) -> None:
        
        if choice == 1:
            print("----Fill updated information----")
            emp_id = int(input("Enter new Employee ID: "))
            first_name = input("Enter new First name: ")
            last_name = input("Enter new Last name: ")
            department_name = input("Enter new Department Name: ")
            rank = input("Enter new rank: ")
            
            new_employee = Employee(emp_id, first_name, last_name, department_name, rank)
            self.__department.add_employee(new_employee)
            print("Employee added successfully!")
            print()
        
        elif choice == 2:
            print("All employees Information: ")
            for employee in self.__department.get_all_employees():
                print("\n")
                print(employee)
        
        elif choice == 3:
            emp_id = int(input("Enter the Employee Id: "))
            print("Employee with that EmpId is:")
            for employee in self.__department.search_employee(emp_id):
                print()
                print(employee)
            print()
        
        elif choice == 4:
            #Not working
            print("Employee information to remove:")
            emp_id = int(input("Enter new Employee ID: "))
            first_name = input("Enter new First name: ")
            last_name = input("Enter new Last name: ")
            department_name = input("Enter new Department Name: ")
            rank = input("Enter new rank: ")

            employee_delete = Employee(emp_id, first_name, last_name, department_name, rank)
            self.__department.remove_employee(employee_delete)
            print("Given employee is successfully removed!")
            print()
        
        elif choice == 5:
            print("Employee information to update:")
            emp_id = int(input("Enter new Employee ID: "))
            first_name = input("Enter new First name: ")
            last_name = input("Enter new Last name: ")
            department_name = input("Enter new Department Name: ")
            rank = input("Enter new rank: ")

            employee_update = Employee(emp_id, first_name, last_name, department_name, rank)
            self.__department.update_employee(employee_update)
            print("Given customer is successfully updated!")
            print()
        
        elif choice == 6:
            print("Add expense:")
            emp_id = int(input("Enter new Employee ID: "))
            date = input("Enter date (YYYY/MM/DD): ")
            amount = int(input("Enter Expense Amount: "))
            category = input("Enter Category: ")
            
            new_expense = Expense(emp_id, date, amount, category)
            print("\n")
            self.__department.add_expense(new_expense)
            print("New expense added")
        
        elif choice == 7:
            print("Show all Expenses: ")
            for expense in self.__department.get_all_expenses():
                print("\n")
                print(expense)
            print()
        
        elif choice == 8:
            print("Delete expense: ")
            emp_id = int(input("Enter existing Employee ID: "))
            date = input("Enter date (YYYY/MM/DD): ")
            amount = int(input("Enter Expense Amount amount to be deleted: "))
            category = input("Enter Category: ")
            
            delete_expense = Expense(emp_id, date, amount, category)
            print("\n")
            self.__department.remove_expense(delete_expense)
            print(f"{delete_expense} expense deleted")
        
        elif choice == 9:
            print("Expense to be updated")
            emp_id = int(input("Enter  Employee ID: "))
            date = input("Enter date (YYYY/MM/DD): ")
            amount = int(input("Enter Expense Amount to be updated: "))
            category = input("Enter Category: ")
            
            update_expense = Expense(emp_id, date, amount, category)
            print("\n")
            self.__department.update_expense(update_expense)
            print(f"{update_expense} expense Updated!")
        
        elif choice == 10:
            print("Show all Departments: ")
            for department in self.__departmentManager.get_all_departments():
                print("\n")
                print(department)
            print()
        
        elif choice == 11:
            print("Add a Department: ")
            dept_name = input("Enter new department: ")
            self.__departmentManager.add_department(dept_name)
            print("Department Added")
            print()
        
        elif choice == 12:
            print("Update a Department: ")
            old_name = input("Enter existing department: ")
            updated_name = input("Enter the new department: ")
            self.__departmentManager.update_department(old_name, updated_name)
            print("Given department is successfully updated!")
            print()
        
        elif choice == 13:
            print("Delete Department")
            delete = input("Enter the dept to delete: ")
            self.__departmentManager.remove_department(delete)
            print("The Department has been deleted")
  
        elif choice == 0:
            print("Thank you for using my app CFO!")
            return choice
        else:
            print("Invalid option selected! Select again!")
            
def main():
    app = ExpenseTracker()
    while True:
        app.show_menu()
        choice = app.get_user_choice()
        if app.process_command(choice) == 0:
            break

if __name__ == "__main__":
    main()
 