class Employee:
    no_of_users=0#class variable
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.email = firstname+'_'+lastname+'@company.com'
        self.pay = pay
        Employee.no_of_users+=1

    def printEmail(self):
        return self.firstname+'_'+self.lastname+'@company.com'

print (Employee.no_of_users)

emp1=Employee("Test","user",200)
emp2=Employee("Demo","user",300)
print(emp1.email)
print(Employee.no_of_users)

print(emp2.printEmail())

print(Employee.printEmail(emp1))

