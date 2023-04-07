import sys
sys.path.append('./')
from components.employee import Employee
from components.expense import Expense
from database.employeeDB import EmployeeRepository
from database.expenseDB import ExpenseRepository


class Department:
    def __init__(self, dept_name: str) -> None:
        self.__dept_name = dept_name
        self.__employees_db = EmployeeRepository()
        self.__expense_db = ExpenseRepository()
        self.__employees: list[Employee] = self.__employees_db.read_employees()
        self.__expenses: list[Expense] = self.__expense_db.read_expenses()
        
    @property
    def dept_name(self) -> str:
        return self.__dept_name
    
    #Get the list of all employees
    def get_all_employees(self) -> list[Employee]:
        return self.__employees
    
    #Add employee to the department
    def add_employee(self, employee: Employee):
        self.__employees.append(employee)
        self.__employees_db.write_employees(self.__employees)
    
    #Remove employee to the department
    def remove_employee(self, employee: Employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
            self.__employees_db.write_employees(self.__employees)
        else:
            print(f"Employee not found!")
    
    #Search employee with unique empId
    def search_employee(self, empId: int):
        search_list: list[Employee] = []
        for employee in self.__employees:
            if employee.emp_id == empId:
                search_list.append(employee)
        
        return search_list
    
    #Update the employee
    def update_employee(self, employee: Employee) -> None:
        if employee in self.__employees:
            print("----Fill updated information----")
            new_emp_id = int(input("Enter new Employee ID: "))
            new_first_name = input("Enter new First name: ")
            new_last_name = input("Enter new Last name: ")
            new_department_name = input("Enter new Department Name: ")
            new_rank = input("Enter new rank: ")
        
            updated_employee = Employee(
                new_emp_id, new_first_name, new_last_name, new_department_name, new_rank
            )
            
            old_index = self.__employees.index(
                employee
            ) # take the index of the given employee
            
            self.__employees[
                old_index
            ] = updated_employee # updated employee goes in the old index
            
            self.__employees_db.write_employees(self.__employees)
        else:
            print(f"Could not find employee")
        
    @property
    def __iter__(self):
        self.__iter_index = 0
        return self
    
    @property
    def __next__(self):
        if self.__iter_index >= len(self.__employees):
            raise StopIteration
        else:
            employee = self.__employees[self.__iter_index]
            self.__iter_index += 1
            return employee
    
    #Get the list of all expenses
    def get_all_expenses(self) -> list[Expense]:
        return self.__expenses

    # Add new expense
    def add_expense(self, expense: Expense):
        self.__expenses.append(expense)
        self.__expense_db.write_expenses(self.__expenses) #update the expense csv
        print(f"Expense named {expense} was added!")
    
    def remove_expense(self, expense: Expense) -> None:
        if expense in self.__expenses:
            self.__expenses.remove(expense)
            self.__expense_db.write_expenses(
                self.__expenses
            ) # this line updates the list where expense is removed
            print(f"Expense named{expense} was deleted!")
        else:
            print(f"Expense not found!")
    
    def update_expense(self, expense: Expense) -> None:
        if expense in self.__expenses:
            print("---Let's update the expense---")
            new_emp_id = int(input("Enter new EmployeeId: "))
            new_date = input("Enter new date: ")
            new_amount = int(input("Enter the updated amount: "))
            category = input("Enter new category: ")
            
            updated_expense = Expense(
                new_emp_id, new_date, new_amount, category
            )

            old_index = self.__expenses.index(
                expense
            )  # take the index of the given expense

            self.__expenses[
                old_index
            ] = updated_expense  # updated expense goes in the old index

            self.__expense_db.write_expenses(self.__expenses)
            print(f"Expense named {expense} was updated!")
        else:
            print(f"Could find the expense!")
    
    # def per_change(self, expense: Expense) -> None:
    # if expense in self.__expenses:
    #     print("---Let's update the expense---")
    #     percentage = int(input("Enter the percentage change: "))
    #     expense.amount *= (1 + percentage / 100)
    #     self.__expense_db.write_expenses(self.__expenses)
    #     print(f"Expense named {expense} was updated!")
    # else:
    #     print(f"Could not find the expense!")

    @property
    def __iter__(self):
        self.__iter_index = 0
        return self

    @property
    def __next__(self):
        if self.__iter_index >= len(self.__expenses):
            raise StopIteration
        else:
            expense = self.__expenses[self.__iter_index]
            self.__iter_index += 1
            return expense
