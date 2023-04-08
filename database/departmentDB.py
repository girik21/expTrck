import sys
sys.path.append('./')
from components.department import Department
import csv

class DepartmentReposiory:
    def __init__(self, filename:str = "./csv/department.csv" ) -> None:
        self.__filename = filename

    #read department data from csv file
    def read_department(self) -> list[Department]:
        departments: list[Department] = []
        
        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
        
            for row in reader:
                department = Department(row[0])
                departments.append(department)
        
        return departments
    
    #write department data
    def write_department(self, departments: list[Department]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for department in departments:
                writer.writerow(department.get_csv())
    
def main():
    # Test For department Data
    dep_db = DepartmentReposiory()
        
    #test reading departments from repo
    departments = dep_db.read_department()
    for department in departments:
        print(department)
        
    department = Department("one")
    departments.append(department)
        
    # test adding new department
    dep_db.write_department(departments)
     
if __name__ == "__main__":
    main()
            
        
            
        