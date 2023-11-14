#5. Write a program to create a Python class representing a basic employee with attributes like name, id, and

class Employe:
    def __init__(self,name,id,salary,position):
        self.name=name
        self.id=id
        self.salary=salary
        self.position=position

    def display_info(self):
        print(f"Name:{self.name}, ID:{self.id}, salary:{self.salary},Psition:{self.position}")

emp=Employe("Madiha\n"
            ,"1234\n"
            ,"50000\n"
            ,"Software Engineer\n")
emp.display_info()
