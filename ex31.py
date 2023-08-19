print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. take cake")
	print("2. scream at bear")
	
	bear = input("> ")
	
	if bear == "1":
		print("Bear eats your face off good job!")
	elif bear == "2":
		print("The bear eats your legs off. god job!")
	else:
		print(f"well, doing {bear} is probably better.")
		print("Bear runs away.")

elif door == "2":
	print("You stare into the endless abyss at Cthulu's retina")
	print("1. Blueberries")
	print("2. Yellow jacket clothepins")
	print("3. understanding revolvers yelling melodies")
	
	insanity = input("> ")
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("morpheus offers you the red or blue pill, which one do you take?")
		pill = input("> ")
		if pill == 'red':
			print("You exit the matrix. good job")
		elif pill == 'blue':
			print("You wake up like nothing ever happened")
		else:
			print("Agent smith kills you while you're trying to make a decision")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
		

else:
	print("you die, good job")
