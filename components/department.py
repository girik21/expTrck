import sys
sys.path.append('./')
from typing import List
from components.employee import Employee
from components.expense import Expense
from database.employeeDB import EmployeeRepository
from database.expenseDB import ExpenseRepository
import matplotlib.pyplot as plt


class Department:
    def __init__(self, dept_name: str, dept_budget: float) -> None:
        self.__dept_name = dept_name
        self.__dept_budget = dept_budget
        self.__employees_db = EmployeeRepository()
        self.__expense_db = ExpenseRepository()
        self.__employees: list[Employee] = self.__employees_db.read_employees()
        self.__expenses: list[Expense] = self.__expense_db.read_expenses()
        
    @property
    def dept_name(self) -> str:
        return self.__dept_name
    
    @property
    def dept_budget(self) -> float:
        return self.__dept_budget
    
    def __str__(self):
        return f"Department-Name: {self.dept_name}\nDepartment-Budget: {self.__dept_budget}"
    
    def get_csv(self) -> list[str]:
        csv_str: list[str] = [
            self.__dept_name,
            self.__dept_budget
        ]

        return csv_str
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Department):
            return __o.__dept_name == self.__dept_name
        else:
            return False
    
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

    def generate_expense_report_by_month(self) -> dict:
        expenses = self.__expense_db.read_expenses()
        report = {}

        for expense in expenses:
            expense_month = expense.expense_date.strftime("%B %Y")
            if expense_month not in report:
               report[expense_month] = 0
            report[expense_month] += expense.amount

        return report
        
    def get_employee_with_most_expense(self) -> Expense:
        expenses: list[Expense] = self.__expense_db.read_expenses()
        if not expenses:
            return None
        return max(expenses, key=lambda expense: expense.amount)
        
    def get_all_expense_category(self) -> list[Expense]:
        expenses: list[Expense] = self.__expense_db.read_expenses()
        categories = set(expense.category for expense in expenses)
        return list(categories)
        
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
    
    def generate_expense_histogram(self) -> List[Expense]:
        expenses: List[Expense] = self.__expense_db.read_expenses()
        expense_amounts = [expense.amount for expense in expenses]
        num_bins = 10
        plt.hist(expense_amounts, bins=num_bins, edgecolor='black')
        plt.xlabel('Expense Amount')
        plt.ylabel('Frequency')
        plt.title('Employee Expense Histogram')
        plt.show()
        return expenses
    
    def generate_employee_histogram(self) -> List[Employee]:
        employees: List[Employee] = self.__employees_db.read_employees()
        all_depts = [employee.department_name for employee in employees]
        all_ranks = [employee.rank for employee in employees]
        num_bins = 10
        plt.hist(all_depts, bins=num_bins, edgecolor='black')
        plt.hist(all_ranks, bins=num_bins, edgecolor='red')
        plt.xlabel('Blue(Department) and Orange(Rank)')
        plt.ylabel('Number')
        plt.title('Employee Department and Rank Histogram')
        plt.show()
        return employees

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

