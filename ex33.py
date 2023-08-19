

def loop_printer(limit,inc):
	i = 0
	numbers = []
	for i in range(0,limit):
		print(f"At the top i is {i}")
		numbers.append(i)
		
		#i = i + inc
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")


print("The numbers: ")

loop_printer(6,2)
