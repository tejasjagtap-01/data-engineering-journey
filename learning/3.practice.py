# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"

# miles = Dog("Miles", 4)
# miles.description()
# miles.speak("Woof Woof")
# miles.speak("Bow Wow")

# print(Dog.description())

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def speak(self, sound):  # Instance method
        return f"{self.name} says {sound}"

    def __str__(self):  # String representation method
        return f"{self.name} is {self.age} years old"

dog1 = Dog('Mikey','3')
dog1.speak("Woof")


print(dog1.name)
print(dog1.age)
print(dog1.speak("Woof"))
print(dog1.species)
print(dog1)