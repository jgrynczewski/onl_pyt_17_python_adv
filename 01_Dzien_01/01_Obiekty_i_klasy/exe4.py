class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.firstName = first_name
        self.lastName = last_name
        self.__salary = 0

    # setter
    def set_salary(self, salary):
        if type(salary) is int and salary > 0:
            self.__salary = salary

    # getter
    def get_salary(self):
        return self.__salary


employee = Employee(1, "Monika", "Mieszczanska")
employee.set_salary(100)
employee.set_salary("Ala ma kota")
#employee.set_salary(40000)
#print(employee.get_salary())