 # contructor --- replace class method
 # we can pass the value while calling

class person:
     def __init__(self,id,fname,lname,age):
         self.id=id
         self.fname=fname
         self.lname=lname
         self.age=age

     def print_value(self):
         print(self.id,self.fname,self.lname,self.age)

person1=person(101,'vinay','k',30)
person1.print_value()
person2=person(102,'amal','p',31)
person2.print_value()
