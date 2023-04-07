class Employee:
    def __init__(self, emp_id: int, first_name: str, last_name: str, department_name: str, rank: str) -> None:
        self.__emp_id = emp_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department_name = department_name
        self.__rank = rank

    @property
    def emp_id(self) -> int:
        return self.__emp_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def department_name(self) -> str:
        return self.__department_name

    @property
    def rank(self) -> str:
        return self.__rank

    def __str__(self) -> str:
        return f"Employee Id: {self.__emp_id}\nFirst Name: {self.__first_name}\nLast Name: {self.__last_name}\nDepartment: {self.__department_name}\nRank:{self.__rank}"

    def get_csv(self) -> list[str]:
        csv_str: list[str] = [
            str(self.__emp_id),
            self.__first_name,
            self.__last_name,
            self.__department_name,
            self.__rank
        ]

        return csv_str

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Employee):
            return __o.__emp_id == self.__emp_id
        else:
            return False


