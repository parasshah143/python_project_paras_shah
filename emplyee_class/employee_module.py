from typing import Union, Any


class Employee:

    company_name = None  # static or class of the variable
    company_location = None

    def __int__(self):
        self.emp_id = None  # non-static variable
        self.emp_name = None
        self.emp_salary = None
        self.epm_performance = None

    @staticmethod
    def print_my_name():
        print("Paras Shah")

    def display_employee_record(self):
        print(self.emp_id)
        print(Employee.company_name)

    def calculate_bonus(self):
        if self.epm_performance == "A":
            print(self.emp_name)
            bonus = 10
            print(bonus)
            self.emp_salary= ((self.emp_salary * bonus) / 100) + self.emp_salary
            print(self.emp_salary)
        elif self.epm_performance == "B":
            print(self.emp_name)
            print("5%")
        else:
            print("Nothing")
