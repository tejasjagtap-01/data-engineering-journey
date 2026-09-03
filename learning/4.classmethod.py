# Python OOP
class Employee:

    num_of_emps = 0 
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@gmail.com'
        self.pay = pay

        Employee.num_of_emps += 1 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first,  last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Master','Thalapaty', 50000)
emp2 = Employee('Chitram','Joseph',600000)

# Regular Method Code
#Employee.set_raise_amt(1.15) # This act as the class method. This will alter the entire class variable instead of single instance
# emp1.set_raise_amt(1.45) # we can access the class method via instances also

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)


# Class Method Code
# emp_str_1 = 'Johnny-Deo-50000'
# emp_str_2 = 'Captain-Sky-75000'

# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)

# print(new_emp_1.last)
# print(new_emp_1.first)

# print(new_emp_2.last)
# print(new_emp_2.pay)

# Static Method
# import datetime
# my_date = datetime.date(2026, 8, 23)

# print(Employee.is_workday(my_date))