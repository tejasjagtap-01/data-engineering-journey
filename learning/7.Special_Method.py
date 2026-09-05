# Special Method

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '__' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}' , '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    #a method for  adding the all employees salary
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Nivedita','Jagtap',900000)
emp2 = Employee('Vedita','Jagtap',1100000)
emp3 = Employee('Tejas', 'Jagatp',1000000)


# print(emp1.email)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

#The Special methoda
# print(repr(emp1))
# print(str(emp1))


#The DUNDER() for addition
# print(3 + 5)
# print(int.__add__(3,5))
# print(int.__mul__(5, 3))
# print(str.__add__('a','z'))
# print(emp3 + emp2)


#Dunder Method for Length
print(len(emp1))
print(len(emp2))
print(len(emp3))