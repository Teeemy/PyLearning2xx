class Student():
    name = None
    age = None
    id = None
    phone_no = None
    email_address = None
    sex = None

    def eat(self):
        print("Student can eat")

    def sleep(self):
        print("Student can sleep")

    def read(self):
        print("Student can read")

    def what_is_student_name(self):
        print("Name of Student is  " + self.name)

    def how_old_is_student(self):
        print("Age of Student  " + self.age)


suraj = Student()
suraj.name = "suraj"
print(suraj.name)

suraj = Student()
suraj.age = 23
print(suraj.age)

suraj.what_is_student_name()
suraj.how_old_is_student()
