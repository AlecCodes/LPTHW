from sys import exit

def gold_room():
	print("This room is full of gold. how much do you take?")
	
	choice = input("> ")
	if type(int(choice)) == type(1):
		how_much = int(choice)
	else:
		dead("Man learn to type number")
	
	if how_much < 50:
		print("Nice youre not greedy you win")
		exit(0)
	else:
		dead("You greedy bastard")
		

def bear_room():
	print("Theres a bear here")
	print("The bear has huoney")
	print("Bear is in front of another door")
	print("How u going to move da bear")
	bear_moved  = False
	
	while True:
		choice = input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then klils u")
		elif choice == "Taunt bear" and not bear_moved:
			print("The bear moved from the door")
			print("You can go thru it now")
			bear_moved = True
		elif choice == "Taunt bear" and bear_moved:
			dead("The bear gets pissed off an kills u")
		elif choice == "open door" and bear_moved:
			gold_room()	
		else: 
			print("I got no idea what that means")
		
		
def cthulu_room():
	print("here u see cthulu")
	print("u go insane")
	print("do you flee or eat your head?")
	
	choice = input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty")
	else:
		cthulu_room()
		

def dead(why):
	print(why, "good job!")
	exit(0)
	
def start():
	print("your in a dark room")	
	print("door to right and left")
	print("which one do u take?")
	
	choice = input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulu_room()
	else:
		dead("you stumble around until you starve.")


start()
