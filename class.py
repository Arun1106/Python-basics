class Student:
    def __init__(self,name,rollno,mark):
        self.name=name
        self.rollno=rollno
        self.mark=mark
    def add_mail(self):
        self.mail=self.name+"@gmail.com"

    def show(self):
        print("name:",self.name)
        print("mail:",self.mail)
        print("mark:",self.mark)
        print("rollno:",self.rollno)

S1=Student('arun','1718105','55')
S1.add_mail()
S1.show()
print(S1.__dict__)