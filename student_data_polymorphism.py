# I began this code by creating a parent class of student data with a few basic attributes
class Student_data:
    # I used the init method to initialise the student data class with two attributes: name and stream
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # methods within the class which print statements to show what the student is doig
    def info(self):
        print(f"I am a student. My name is {self.name}. I am {self.age} years old.")

    def study(self):
        print(self.name, " is studying")

# this here inherits the methods from student data
class Devops_trainee(Student_data):
    def __init__(self, stream, background):
        super().__init__("Devops", background)
        self.stream = stream
        self.background = background
    #  this overrides method in student_data
    def info(self):
        print(f"I am a DevOps trainee. My name is {self.name}. I am {self.age} years old.")

    def study(self):
        print(self.name, " is coding")



dev = Devops_trainee("Devops", "Politics")

print(dev.study())
print(dev.info())



