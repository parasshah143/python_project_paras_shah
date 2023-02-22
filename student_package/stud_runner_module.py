class Student:
    school_name = None  # static or class of the variable
    school_address = None

    def __init__(self, rollno=None, name=None, mailid=None, percentage=None):
        self.student_rollno = rollno  # non-static variable
        self.student_name = name
        self.student_mailid = mailid
        self.student_percentage = percentage

    @staticmethod
    def print_my_name():
        print("Paras Shah")

    # @property
    def name_with_percentage(self):
        return "Your name " + self.student_name + " Your percentage " + str(self.student_percentage)

    def display_student_record(self):
        print(self.student_rollno)
        print(self.student_name)
        print(self.student_mailid)
        print(self.student_percentage)

    def print_email_id(self):

        if self.student_mailid == "peter@gmail.com":
            replace = self.student_mailid.replace("peter@gmail.com", "jack@gmail.com", )
            print(replace)
        else:
            print(self.student_mailid)
