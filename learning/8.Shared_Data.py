# instance variables are for data unique to each instance.
# class variables are for attributes and methods shared by all instances of the class.
# shared data can have possibly surprising effects involving mutable objects such as lists and dictionaries.

class Dog:

    kind = 'canine' #Class variable

    # instance variable uinque to each instance
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    def add_tricks(self, tricks):
        self.tricks.append(tricks)

Dog1 = Dog('Georg',5)
Dog1.add_tricks('Rolling down: for the Walk or show excitment')

print('The kind of Dog is', Dog1.kind)
print('Dog is', Dog1.age,'Years old')
print('The name of Dog is',Dog1.name)
print(Dog1.tricks)   