import questions
from sys import exit
grade_order = ['kindergarden','first_grade','second_grade','third_grade','fourth_grade','fifth_grade']


class grade(object):
	
	def hold_back(self):
		print ("""BRUH... \nYou couldn\'t pass {} .. You are held back to {} """.format(grade_order[self.grade_number], grade_order[self.grade_number-1]))
		input("Press any key to continue...")

		
		
	def preview(self):
		if self.grade_number < 5:
			print('welcome to ' + grade_order[self.grade_number] + '! Answer this question to progress to ' + grade_order[self.grade_number + 1])
		else:
			print('welcome to ' + grade_order[self.grade_number] + '! Answer this question to progress to fricken GRADUATE!')			


class engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		final_scene = self.scene_map.next_scene('finished')
		while current_scene != final_scene:
			current_scene.preview()
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name) 
		#plays the final scene, will only execute once the while loop terminates, which means the final scene has been reached
		current_scene.enter()
		
		
		
class Kindergarden(grade):
	def __init__(self):
		self.grade_number = 0
	def enter(self):
		input("welcome to kindergarden. press any key to continue. This is a test of your skill. If you cant type a key you're not ready for first grade.")
		return 'first_grade'
		
		
		
		
class FirstGrade(grade):
	def __init__(self):
		self.grade_number = 1
	def enter(self):
		if questions.first_grade_question():
			print("Correct! You're ready for second grade!")
			input("Press any key to continue...") 
			return grade_order[self.grade_number + 1]
		else:
			self.hold_back()
			return grade_order[self.grade_number - 1]
			
			
			
			
class SecondGrade(grade):
	def __init__(self):
		self.grade_number = 2
	def enter(self):
		if questions.second_grade_question():
			print('You passed second grade!')
			input("Press any key to continue...") 
			return grade_order[self.grade_number + 1]
		else:
			self.hold_back()
			return grade_order[self.grade_number - 1]
			
			
			
			
class ThirdGrade(grade):
	def __init__(self):
		self.grade_number = 3
	def enter(self):
		if questions.third_grade_question():
			print("You passed third grade!")
			input("Press any key to continue...")
			return grade_order[self.grade_number + 1]
		else:
			self.hold_back()
			return grade_order[self.grade_number - 1]
			
			
			
			
class FourthGrade(grade):
	def __init__(self):
		self.grade_number = 4
	def enter(self):
		if questions.fourth_grade_question():
			print("You passed fourth grade!")
			input("Press any key to continue...")
			return grade_order[self.grade_number + 1]
		else:
			self.hold_back()
			return grade_order[self.grade_number - 1]
			
			
			
		
class FifthGrade(grade):
	def __init__(self):
		self.grade_number = 5
	def enter(self):
		if questions.fifth_grade_question():
			print("You passed fifth Grade! YOU GRADUATED ELEMENTARY SCHOOL!")
			input("Press any key to throw your graduation cap into the air!")
			print(' ~~~~~~~~~~~~ ^_^  ~~~~~~')
			return 'finished'
		else:
			self.hold_back()
			return grade_order[self.grade_number - 1]	
			
			
				 
class Finished():
	def enter(self):
		print('GG')
		exit(0)

class Map(object):
	#a dictionary of instances of each class, thus allowing the engine to call each grades' enter method
	scenes = {
	grade_order[0] : Kindergarden(),
	grade_order[1] : FirstGrade(),
	grade_order[2] : SecondGrade(),
	grade_order[3] : ThirdGrade(),
	grade_order[4] : FourthGrade(),
	grade_order[5] : FifthGrade(),
	'finished' : Finished(),
	}
	#this allows the play method of engine to have it's opening scene
	def __init__(self, start_scene):
		self.start_scene = start_scene
	#this allows the play method to start the next scene by looking up its 'keyword' in scenes when a grade is completed
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
	
a_map = Map('kindergarden')
e = engine(a_map)
e.play()
