# Python OOP

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.email = first + '_' + last + '@gmail.com'
        self.pay = pay 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.20

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

class Manager(Employee):

    #This will instantiate new method
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    #This will add employee in the employee class
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    #This will allow to remove the element from the employee.
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    #This will print all employees associated to the specific manager
    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())


dev1 = Developer('Jack','Spparow',42600, 'Python')
dev2 = Developer('Tony','Starck',55000, 'DOTNeT')
dev3 = Developer('Peter','Parker',55000, 'Java')
dev4 = Developer('Roma','Finch',55000, 'Kotlin')
dev5 = Developer('Pete','Juli',55000, 'C++')

# print(dev2.email)
# print(dev1.email)

# print(help(Developer))
#print(help(Manager))
# print(help(Employee))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(dev2.pay)
# dev2.apply_raise()
# print(dev2.pay)

# print(dev1.email)
# print(dev1.pay)
# print(dev1.prog_language)

man1 = Manager('Che','Guvera',50000, [dev1, dev2])
man2 = Manager('Robert','Oppenheimer',90000, [dev4, dev3])
man3 = Manager('Chistopher', 'Nolan', 110000, [])

print(man1.email)
man1.add_emp(dev5) # It add new employee in the list
man1.remove_emp(dev1) # It remover employee in the list
man1.print_emps()

print(man2.email)
man2.print_emps()

print(man3.email)
man3.add_emp(dev1)
man3.print_emps()