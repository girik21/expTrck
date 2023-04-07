from datetime import datetime

class Expense:
    def __init__(self, employee_id: int, date: str, amount: int, category: str) -> None:
        self.__emp_id = employee_id
        self.__date = datetime.strptime(date, "%Y-%m-%d").date()
        self.__amount = amount
        self.__category = category
    
    @property
    def expense_date(self) -> str:
        return self.__date
    
    @property
    def amount(self) -> int:
        return self.__amount
    
    @property
    def category(self) -> str:
        return self.__category
    
    @property
    def employee_id(self) -> int:
        return self.__emp_id
    
    def __str__(self) -> str:
        return f"Employee Id: {self.__emp_id}\nDate: {self.__date}\nAmount: ${self.__amount}\nCategory: {self.__category}"

    def get_csv(self) -> list[str]:
        csv_str: list[str] = [
            str(self.__emp_id),
            self.__date,
            str(self.__amount),
            self.__category,
        ]

        return csv_str

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Expense):
            return __o.__emp_id == self.__emp_id
        else:
            return False


