#1. Implement a Python class representing a student with a constructor and methods for setting and getting 
student details.

class Student:
    def __init__(self, name=None,rlno=None,age=None,marks=None):
        self.name=name
        self.rlno=rlno
        self.age=age
        self.marks=marks

    def setAge(self,age):
        self.age=age

    def setMarks(self,marks):
         self.marks=marks

    def Display(self):
        print("student Name is::",self.name)
        print("Student RollNo is::",self.rlno)
        print("Student Age is::",self.age)
        print("Student Marks is::",self.marks)
        

std=Student("Madiha Mulla",75)
std.setAge(19)
std.setMarks(50)
std.Display()
