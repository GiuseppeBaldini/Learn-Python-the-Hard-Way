## Animal is-a object
class Animal(object):

    def __init__(self, color):
        self.color = color


## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name of some kind
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name as well
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary (hopefully)
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named "Satan"
mary.pet = satan

## Frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named "Rover"
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
