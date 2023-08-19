##Animal is-a object
class Animal(object):
	def print_name(self):
		print(self.name)
##Dog is a animal
class Dog(Animal):
	
	def __init__(self,name):
	## dog has a name attribute
		self.name = name	
	
## Cat is a animal
class Cat(Animal):

	def __init__(self,name):
	##cat has a name
		self.name = name
	
## person is a object
class Person(object):

	def __init__(self,name):
		## person has a name
		self.name = name
		
		## person has a pet of some kind		
		self.pet = None
	def walk(self):
		print("walking like human")
		
## employee is a person
class Employee(Person):
	
	def __init__(self,name,salary):
		## calls init method from parent class
		super(Employee,self).__init__(name)
		## employee has a salary
		self.salary = salary

## Fish is a object
class Fish(object):
	def speak(self):
		print("glub blub")

## salmon is a fish
class Salmon(Fish):
	pass
		

class Halibut(Fish):
	pass


## rover is a dog
rover = Dog("Rover")


## satan is a cat
satan = Cat("Satan")

##mary is a person
mary = Person("Mary")

##mary has a pet
mary.pet = satan

## frank is a employee
frank = Employee("Frank",120000)

## frank has a pet
frank.pet = rover

## Flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()

class fishman(Person, Fish):
	pass

abe = fishman("abe")
abe.speak()
abe.walk()
