class Emp:
    def __init__(self,name,emp_number):
        self.name=name
        self.emp_number=emp_number
    def getdetails(self):
        print(self.name)
        print(self.emp_number)
    
class Details(Emp):
    def __init__(self,name,emp_number,salary):
        Emp.__init__(self,name,emp_number)
        self.salary=salary*1.05
    def salary_details(self):
        return self.salary
Emp1=Details('arun','100',5000)
Emp1.getdetails()
print(Emp1.salary_details())


