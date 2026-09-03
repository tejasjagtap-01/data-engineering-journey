#Day1

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('tejas','jagtap','90k')
emp2 = Employee('coca','cola','85k')
emp3 = Employee('master','Johan','100k')
emp4 = Employee('Max','Versttapan','200k')

#print(emp1.email)
#print(emp2.email)
#print(emp2.pay)
#print(emp3.email , ' & ',emp3.pay)

#print('{} {}'.format(emp1.first, emp1.last)) # to print the name & last name together
#print('{} {}'.format(emp3.first, emp2.last))

#print(emp4.fullname()) #Print via Using the fullname() method
#print(emp2.fullname())

#print(emp1.fullname())
#print(Employee.fullname(emp4))

print(Employee.fullname(emp2))

## Without Class
#emp1 = Employee()
#emp2 = Employee()

#print(emp1)
#print(emp2)

#emp1.first = 'talha'
#emp1.last = 'anjum'
#emp1.email = 'talha_anjum92@gmail.com'
#emp1.pay = 60606

#emp2.first = 'talha'
#emp2.last = 'anjum'
#emp2.email = 'talha_anjum92@gmail.com'
#emp2.pay = 70767

#print(emp1.pay)
#print(emp2.pay)

#print(emp1.first)
#print(emp2.first)

