def student_mark(marks):
    if marks >= 90:
        print("Grade A")
    elif 80 <= marks <= 89:
        print("Grade B")
    elif 60 <= marks <= 79:
        print("Grade C")
    elif 45 <= marks <= 59:
        print("Grade D")
    elif marks < 45:
        print("Grade D")
    else:
        print("Wrong Input")
    return "Done"
