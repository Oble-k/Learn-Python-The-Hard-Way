# Is-a, Has-a, Objects and Classes
# Animal is-a object
class Animal(object):
    pass

# Dog is-a Animal that is-a object
class Dog(Animal):

    def __init__(self, name):
        # Dog (self) has-a name
        self.name = name
# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name
# Person is-a object
class Person(object):
    def __init__(self, name):
        #Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):

        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass
# Salmon is-a Fish
class Salmon(Fish):
    pass
#Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")
# Satan is-a cat
satan = Cat("Satan")
# Mary is-a person
mary = Person("Mary")
# Frank is-a Employee. Frank has-a 120000 salary
frank = Employee("Frank", 12000)
# frank has-a pet
frank.pet = rover
# Flipper is-a instance of the Fish class
flipper = Fish()
# crouse is-a instance of the Salmon class
crouse = Salmon()
# Harry is-a instance of the Halibut class
harry = Halibut()