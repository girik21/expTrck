import sys
sys.path.append('./')
from components.department import Department
from database.departmentDB import DepartmentRepository
import matplotlib.pyplot as plt
from typing import List

class DepartmentManager:
    def __init__(self) -> None:
        self.__department_db = DepartmentRepository()
        self.__departments: list[Department] = self.__department_db.read_department()
    
    def get_all_departments(self) -> list[Department]:
        print()
        return self.__departments
    
    def add_department(self, department_name: str, department_budget: float):
        department = Department(department_name, department_budget)
        self.__departments.append(department)
        self.__department_db.write_department(self.__departments)
        print()
        print(f"{department_name} added to departments list")

    def remove_department(self, department_name: str):
        for index, department in enumerate(self.__departments):
            if department.dept_name == department_name:
               self.__departments.remove(department)
               self.__department_db.write_department(self.__departments)
               print(f"{department_name} removed from departments list")
               return
        print()
        print(f"{department_name} not found in departments list")
    
    def update_department(self, department_name: str, new_department_name: str, department_budget: float, new_department_budget: float):
        for index, department in enumerate(self.__departments):
            if department.dept_name == department_name:
                new_department = Department(new_department_name, new_department_budget)
                self.__departments[index] = new_department
                self.__department_db.write_department(self.__departments)
                print(f"{department_name} updated to {new_department_name} in departments list")
                return
        print()
        print(f"{department_name} not found in departments list")
    
    def search_department(self, depart_name: int):
        search_list: list[Department] = []
        for department in self.__departments:
            if department.dept_name == depart_name:
                search_list.append(depart_name)
        
        return search_list
    
    def get_department_with_highest_budget(self) -> list[Department]:
        sorted_departments = sorted(self.__departments, key=lambda d: d.dept_budget, reverse=True)
        if sorted_departments:
            return sorted_departments[0]
        return None
    
    def generate_department_histogram(self) -> List[Department]:
        departments: List[Department] = self.__department_db.read_department()
        department_expenses = [department.dept_budget for department in departments]
        num_bins = 10
        plt.hist(department_expenses, bins=num_bins, edgecolor='black')
        plt.xlabel('Department Monthly Budget', fontsize=24)
        plt.ylabel('Frequency', fontsize=14)
        plt.title('Department Expense Histogram', fontsize=26)
        plt.show()
        return departments
    
    def get_total_capital(self) -> float:
        departments: List[Department] = self.__department_db.read_department()
        total_expense = 0.0
        for department in departments:
            total_expense += department.dept_budget
        return f"The Total budget of the company is ${total_expense}"
            

            

