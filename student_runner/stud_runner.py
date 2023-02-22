from student_package.stud_runner_module import Student


def class_runner():
    Student.school_name = "Global school"
    Student.school_address = "chennai"

    print(Student.school_name)
    print(Student.school_address)

    # objects
    # student1 = student(1001,"jack",jack@gmail.com,45.2, Global school, chennai)
    # student2 = student(1002,"peter",peter@gmail.com,85.2, Global school, chennai)
    # student3 = student(1003,"mark",mark@gmail.com,56.5, Global school, chennai)

    student1 = Student(1001, "jack", "jack@gmail.com", 45.2)
    student2 = Student()
    student3 = Student()

    # student1.student_rollno = 1001
    # student1.student_name = "jack"
    # student1.student_mailid = "jack@gmail.com"
    # student1.student_percentage = 45.2

    student2.student_rollno = 1002
    student2.student_name = "peter"
    student2.student_mailid = "peter@gmail.com"
    student2.student_percentage = 85.2

    student3.student_rollno = 1003
    student3.student_name = "mark"
    student3.student_mailid = "mark@gmail.com"
    student3.student_percentage = 56.5

    # To call static method we have to follow below syntax
    Student.print_my_name()

    # To call non-static method we have to follow below syntax
    student1.display_student_record()
    student2.display_student_record()
    student3.display_student_record()

    student1.print_email_id()
    student2.print_email_id()
    student3.print_email_id()

    output = student1.name_with_percentage()
    print(output)
