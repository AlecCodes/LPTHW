from sys import exit
from random import randint
import hangman


class Scene(object):
	def enter(self):
		print("This scene not yet configured. Subclass it and implement enter()")
		exit(1)

class Engine(object):
	#engine is initalized with map as param. An instance of Map class should be passed as argument into Engine(), so we can make an instance of engine and call play() to start game.
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
	#calls the opening_scene method of Map class, which at first returns an instance of the CentralCorridor class. This is saved in variable current_scene. value will change as scenes return different keywords... right?
		print("opening scene")
		current_scene = self.scene_map.opening_scene()
		#final_scene is a variable assigned to an instance of the Finished class. 
		final_scene = self.scene_map.next_scene('finished')

		while current_scene != final_scene:
			print("tteest")
			#The user gives an input, and the returned keyword is set to next_scene_name.
			next_scene_name = current_scene.enter()
			#current_scene local variable is updated to whatever the next scene will be 
			current_scene = self.scene_map.next_scene(next_scene_name)
		#Remember, this block will only execute only if (current_scene == final_scene) 
		current_scene.enter()
		
class Death(Scene):
	def enter(self):
		print("You die!!")
		exit(0)
		
class CentralCorridor(Scene):
	def enter(self):
		#funny = randint(0,1)
		print('before you stands a goron.. tell him a joke if you want to live (hint: his name is dong and does not like it when people joke about his name..)')
		joke = str(input("> "))
		if "dong" not in joke:
			print('so funny i forgot to laugh... prepare to die..')
			return 'death'
		else:
			print("\"" + str(joke) + "\"" + '....hee heee. ... heee hee... very funny!!')
			return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
	def enter(self):
		self.num1 = randint(0,3)
		self.num2 = randint(0,3)
		print("Welcome to the laser armory. to obtain a plasma grenade you must pass an intelligence check. what is {} plus {} ?".format(self.num1, self.num2))
		if int(input("> ")) == self.num1 + self.num2:	
			return 'the_bridge'
		else:
			print("insufficient intellegence. TERMINATE")
			return 'death'

class TheBridge(Scene):
	def enter(self):
		print("""You enter the bridge. \n Before you stands a cyborg. \n Type 1 to attack, Type 2 to evade""")
		action = int(input("> "))
		if action == 2:
			return 'escape_pod'
		else:
			print("Cyborg karate chops your head off")
			return 'death'
								

class EscapePod(Scene):
	def enter(self):
		print('You must complete a game of hangman to enter escape pod :P')
		hangman.crossplay()


class Finished(Scene):
	def enter(self):
		print('you won!!')
		return 'finished'

class Map(object):

	scenes = {
	'central_corridor':CentralCorridor(),
	'laser_weapon_armory':LaserWeaponArmory(),
	'the_bridge':TheBridge(),
	'escape_pod':EscapePod(),
	'death':Death(),
	'finished':Finished()
	}
	#initializes the attribute start_scene. This establishes the first scene of the game, so it can be called by opening_scene, which in turn calls next_scene.
	def __init__(self, start_scene):
		self.start_scene = start_scene
	#takes scene_name param and creates an INSTANCE of corresponding value in scenes. This is val. Misleading name, it doesn't skip to the next scene!!
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	#calls next_scene and passes the start_scene as param. This way calling opening_scene(central_corridor) wil return CentralCorridor() 
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
