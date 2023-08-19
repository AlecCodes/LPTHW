from random import randint
from sys import exit

#strip non printing characters, use an online tool 

words = ['headphone', 'monkey', 'valhalla', 'flavortown', 'orange']

class hangman(object):
	def __init__(self):
		self.line1 = '---------'
		self.line2 = '---------'
		self.line3 = '---------'
		self.line4 = '---------'
	def add_head(self):
		self.line1 = '----O----'
	def add_torso(self):
		self.line2 = '----+----'
	def add_left_arm(self):
		self.line2 = '---~+----'
	def add_right_arm(self):
		self.line2 = '---~+~---'
	def print_hangman(self):
		print(self.line1)
		print(self.line2)
		print(self.line3)
		print(self.line4)


class engine(object):
	def __init__(self, score):
		self.score = score
	def start_game(self):
		new = hangman()

class prompts(object):
	def __init__(self, gallow):
		self.gallow = gallow
		self.word = words[randint(0,4)]
		self.spacelist = ['_' for i in range(len(self.word))]
	def guess(self):
		losecount = 0
		wincount = 0
		while losecount < 4 and ''.join(self.spacelist) != self.word: 
			print("guess a letter!")
			#print(self.word)
			print(self.spacelist)
			self.guess = str(input("> "))
			if len(self.guess) == 1 and self.guess in self.word:
				for position,letter in enumerate(self.word):
					 if self.word[position] == self.guess:
					 	self.spacelist[position] = self.guess
				print("correct!")
			elif self.guess not in self.word:
				print('Incorrect!')
				losecount += 1
				if losecount == 1: 
					self.gallow.add_head()
				elif losecount == 2:
					self.gallow.add_torso()
				elif losecount == 3:
					self.gallow.add_left_arm()
				elif losecount == 4:
					self.gallow.add_right_arm()
				self.gallow.print_hangman()
		if ''.join(self.spacelist) == self.word:
			print('The word was ' + self.word +'! YOU WIN! GG')
			return 'win'
		elif losecount == 4:
			print('you lose! F')
			return 'lose'
		print('game over!')

def crossplay():
	game1 = hangman()
	start = prompts(game1)
	result = start.guess()
	if result == 'win':
		return 'finished'
	return 'death'

if __name__ == "__main__":		
	game1 = hangman()
	start = prompts(game1)
	start.guess()
#		line1 = '----O----'
#		line2 = '---~+~---'
#		line3 = '----|----'
#		line4 = '---L-L---'
