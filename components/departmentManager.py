import sys
sys.path.append('./')
from components.department import Department
from database.departmentDB import DepartmentRepository

class DepartmentManager:
    def __init__(self) -> None:
        self.__department_db = DepartmentRepository()
        self.__departments: list[Department] = self.__department_db.read_department()
    
    def get_all_departments(self) -> list[Department]:
        return self.__departments
    
    def add_department(self, department_name: str):
        department = Department(department_name)
        self.__departments.append(department)
        self.__department_db.write_department(self.__departments)
        print(f"{department_name} added to departments list")

    def remove_department(self, department_name: str):
        for department in self.__departments:
            if department.dept_name == department_name:
               self.__departments.remove(department)
               self.__department_db.write_department(self.__departments)
               print(f"{department_name} removed from departments list")
            return
        print(f"{department_name} not found in departments list")
    
    def update_department(self, department_name: str, new_department_name: str):
        for index, department in enumerate(self.__departments):
            if department.dept_name == department_name:
                new_department = Department(new_department_name)
                self.__departments[index] = new_department
                self.__department_db.write_department(self.__departments)
                print(f"{department_name} updated to {new_department_name} in departments list")
                return
        print(f"{department_name} not found in departments list")

