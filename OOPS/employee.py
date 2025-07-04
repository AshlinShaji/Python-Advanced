# Employee
#
# id,fname,lname,Gender,dept,comp_name

class employee:
    comp_name='TCS'
    dept='DATA ANALYST'
    def details(self,id,fname,lname,gender):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.gender=gender

    def print_value(self):
        print(self.id,self.fname,self.lname,self.gender,employee.dept,employee.comp_name)

e1=employee()
e1.details('004','Arun','Babu','Male')
e1.print_value()

e2=employee()
e2.details('005','Athul','Baby','Male')
e2.print_value()