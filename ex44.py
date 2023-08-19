class Parent(object):

	def override(self):
		print("PARENT override()")

	def implicit(self):
		print("PARENT implicit()")
	
	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def override(self):
		print("CHILD override()")
	
	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()
#wont override
dad.implicit()
son.implicit()
#son will override
dad.override()
son.override()
#son will override 
dad.altered()
son.altered()
