class   Student:
    #constructor to initialize students

    def __init__(self, name, registration_number):
        
        # students name and registration 
        self.name = name
        self.registration_number = registration_number

    def student_info(self):
        # student information
        print(f"Student Name: ", self.name)
        print(f"registration_number: ", self.registration_number)

# examples of students
student1 = Student("naturinda patrah", "registration_001")
student1.student_info()

student2 = Student("Kushivans", "registration_002")
student2.student_info()

student3=Student("brian","registration_003")
student3.student_info()
