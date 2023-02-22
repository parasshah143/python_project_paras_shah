# Main Python File

from math_runner import runner
from mark import grade
from emplyee_class import employee_runner
from student_runner import stud_runner
from browser_launch import launch

if __name__ == '__main__':
    runner.area_of_all()
    print("All calculations are completed successfully")
    mail_id = "paras.shah@gmail.com"
    print(mail_id.split("@")[0])
    Mark = 79
    print(grade.student_mark(Mark))
    employee_runner.class_runner()
    stud_runner.class_runner()
    launch.launch_browser()
