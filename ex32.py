the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this is the kind of for loop goes thru a list
for number in the_count:
	print(f"This is count {number}")
	
# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")
	
#also iterate mixed lists
for i in change:
	print(f"I got {i}")

#we can build lists
elements = []

#then use the range function
for i in range(0,6):
	print(f"Adding {i} to the list")
	
	elements.append(i)


for i in elements:
	print(f"Element was: {i}")

ex = range(0,6)
for i in ex:
	print(i)
