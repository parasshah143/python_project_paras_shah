from emplyee_class.employee_module import Employee


def class_runner():
    Employee.company_name = "EInfoChips"
    Employee.company_location = "Ahmedabad"

    print(Employee.company_name)
    print(Employee.company_location)

    # objects
    # emp1 = Employee(1, 'Paras Shah', 1000, 'A')
    # emp2 = Employee(2, 'Paras Shah', 1000, 'A')
    # emp3 = Employee(3, 'Paras Shah', 1000, 'A')

    emp1 = Employee()
    # emp2 = Employee()
    # emp3 = Employee()
    print(emp1)

    emp1.emp_id = 1
    emp1.emp_name = "Paras"
    emp1.emp_salary = 2000
    emp1.epm_performance = "A"
    print("hi")
    print(emp1.emp_id)

    # To call static method we have to follow below syntax
    Employee.print_my_name()

    # To call non-static method we have to follow below syntax
    emp1.display_employee_record()

    emp1.calculate_bonus()
