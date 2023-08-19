from sys import exit

dracula_mood = "Neutral"	

def start():
	print("You are in dracula's castle. You can't remember why you're there in the first place.")
	print("What is your next move?")
	print("1 - eat a bat, 2 - call 911, 3 - meditate")
	choice = input("> ")
	
	if choice == "1":
		bat_mode()
	elif choice == "2":
		police_helicopter()
	elif choice == "3":
		astral_project()
	else:
		dead("Dracula kills you.")

def dead(why):
	print(why, "RIP")
	exit(0)

def victory():
	print("You WIN! GG")
	exit(0)

def bat_mode():
	global dracula_mood
	print("You eat the juicy bat. Black hairy wings grow out of your back and your ears grow tall and pointy")
	dracula_mood = "Pleased"
	print(f"current Dracula mood: {dracula_mood}")
	room1()
	
def police_helicopter():
	global dracula_mood
	print("The 911 dispatcher tells you that a helicopter is on the way.")
	dracula_mood = "Angry"
	print(f"current Dracula mood: {dracula_mood}")
	room1()

def astral_project():
	global dracula_mood
	print("You sit cross legged on the slimy cold stone ground. The ground beneath you turns into a lotus flower and sunlight shoots out of your forehead. you now have a bird's eye view of dracula's castle")
	dracula_mood = "Scared"
	print(f"current Dracula mood: {dracula_mood}")
	room1()	

def room1():
	print("There are two doors before you. Which one do you open?")
	print("1 - open left door to torture chamber, 2 - open right door to ball pit")
	choice = input("> ")
	if choice == '1':
		torture_chamber()
	elif choice == '2':
		ball_pit()
	else:
		room1()	
		
def torture_chamber():
	print("You enter the torture chamber...")
	if dracula_mood == "Angry":
		print("Dracula falls from the ceiling and feeds you to the rats")
		dead("Damn...")
	elif dracula_mood == "Pleased":
		print("Dracula falls from the ceiling. \"I would never tortue a bat!\" he says. Dracula then invites you to his ball pit")
		ball_pit()
	else:
		print("Dracula falls from the ceiling. He is scared of your enlightenment. Do you: ")
		print("1 - drive a stake through his heart, 2 - show mercy")
		choice = input("> ")
		if choice == "1":
			print("You kill Dracula.")
			victory()
		elif choice == "2":
			print("Dracula thanks you for sparing him. As a token of his graditude, he invites you to the ball pit.")
			ball_pit()
		else:
			print("Not a valid input")
			dead("Dracula kills you")
			
def ball_pit():
	print(dracula_mood)
	print("Welcome to the ball pit...")
	
#def print_mood():
#	print(f"current Dracula mood: {dracula_mood}")
	
start()
