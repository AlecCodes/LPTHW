def add(a,b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a,b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a,b):
	print(f"Multiplying {a} * {b}")
	return a * b

def divide(a,b):
	print(f"DIVIDING {a}/{b}")
	return a / b
	

print("Lets do some math w funcitons!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height {height}, Weight: {weight}, IQ: {iq}")



print("heres a puzzle")

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print(what)
print(35 + (74 - (25*180))) 

def linear (x, m, b):
	return add(multiply(m,x),b)
	
print(linear(3,2,2)) 
