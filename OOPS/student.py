class Student:
    def details(self,f_name,l_name,course,Gender,coll_number):
        self.f_name=f_name
        self.l_name=l_name
        self.course=course
        self.Gender=Gender
        self.coll_number=coll_number
    def print_value(self):
        print(self.f_name,self.l_name,self.course,self.Gender,self.coll_number)
s1=Student()
s1.details('Ashlin','Shaji','CSE','Male','001')
s1.print_value()

s2=Student()
s2.details('Ashique','Abu','Physics','Male','002')
s2.print_value()

s3=Student()
s3.details('Sandra','John','Chemistry','Female','003')
s3.print_value()

s4=Student()
s4.details('Aleena','Johny','CSE','Female','004')
s4.print_value()