class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '_' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'. format(self.first, self.last) 

    def applyraise(self):
        self.pay = int(self.pay * Employee.raise_amount) # self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp1 = Employee('Johan','Maxmuller', 90000)
emp2  = Employee('Mozart','Gothe',45000)

print(Employee.num_of_emps)

print(emp1.pay)
emp1.applyraise()
print(emp1.pay)



# emp1.raise_amount = 1.06

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(emp1.__dict__)
# print(Employee.__dict__)