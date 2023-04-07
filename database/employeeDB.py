import sys
sys.path.append('./')
from components.employee import Employee
import csv

class EmployeeRepository:
    def __init__(self, filename:str = "./csv/employee.csv" ) -> None:
        self.__filename = filename

    #read employee data from csv file
    def read_employees(self) -> list[Employee]:
        employees: list[Employee] = []
        
        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
        
            for row in reader:
                employee = Employee(int(row[0]), row[1], row[2], row[3], row[4])
                employees.append(employee)
        
        return employees
    
    #write employee data
    def write_employees(self, employees: list[Employee]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for employee in employees:
                writer.writerow(employee.get_csv())
    
def main():
    # Test For Employee Data
    emp_db = EmployeeRepository()
        
    #test reading employees from repo
    employees = emp_db.read_employees()
    for employee in employees:
        print(employee)
        
    employee = Employee(3, "John", "Doe", "Brit-1", "SPY")
    employees.append(employee)
        
    # test adding new employees
    emp_db.write_employees(employees)
     
if __name__ == "__main__":
    main()
            
        
            
        