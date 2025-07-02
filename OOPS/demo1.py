class Person:
    def setvalue(self,first_name,last_name,age,gender,phno):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.phno=phno
    def printvalue(self):
        print(self.first_name,self.last_name,self.age,self.gender,self.phno)
person1=Person()
person1.setvalue('vinay','k',26,'Male',97658439220)
person1.printvalue()
# print("*"*100)
person2=Person()
person2.setvalue('Anu','M',23,'Female',97658439786)
person2.printvalue()