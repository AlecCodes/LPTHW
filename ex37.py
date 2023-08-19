global nosix
nosix = []

class dict_maker:
	def __init__(self,lst):
		self.lst = lst
	
	def make_d(self):
		d = {}
		for i,v in enumerate(self.lst):
			d[v] = int(v)**2
		print(d)
		
while len(nosix) < 3:
	choice = input("enter a number that's not 6 > ")

	try:
		int(choice)
		if '6' == choice:
			raise ValueError
		print("Adding " + str(choice) + " to list...")
		nosix.append(choice)
		
	except ValueError as e:
		print(e, "not a valid input!!")


dict1 = dict_maker(nosix)
dict1.make_d()

print("Well hello \a \a \a \a \a there my name is slash a")
print("Well hello \b there im backspace")
print("Well hello \f there im formfeed")
print("Well hello \n there im newline")
print("Well hello \r there im carriage")
print("Well hello \t there im tab")
print("Well hello \v there im vertical tab")
