#TO DO - make result() print the grid without more, or less, yellow guesses than the user provides. Also, if user guess yields a green character, that shouldn't appear elsewhere in the result list as a yellow. No redundant yellows! 
 
from random import randint
from sys import exit

words = ['sinus','motto','sorry','fryer','frodo','sassy']


class play(object):
	def __init__(self):
		self.word = words[randint(0,4)]
		self.clues = ['_','_','_','_','_']
	
	#def input(self):
	#	print("Guess a five letter word!")
	#	self.guess = input("> ")
	#	return self.guess
	
	def printword(self):
		print(self.word)
		
	def result(self, attempt):
		yellowcount = 0
		for i,v in enumerate(attempt):
			if v == self.word[i]:
				self.clues[i] = v.capitalize()
			elif v in self.word and v != self.word[i]:
				for letter in self.word:
					if letter in  
					
					yellowcount += 1 
					self.clues[i] = v.lower()
				

		print(self.clues)
	
	def result2(self,attempt):
		match_list = []
		guess_list = []
		yellow_list = []
		#know the amount of yellow guesses per attempt		
		for i,v in enumerate(attempt):
			if v == self.word[i]:
				self.clues[i] = v.capitalize()
				match_list.append(v)
			elif v in self.word and not in match_list:
				yellow_list.append(v)
				
				
			
		print(guess_list)
			
				
				
	def start(self):
		losecount = 0
		print("Guess a five letter word! hint: the word is..")
		self.printword()
		guess = input("> ")
		while guess != self.word:
			losecount += 1
			self.result(guess)
			print(str(10-losecount) + ' Guesses remain!')
			guess = input("Try another word! > ")
			if losecount == 10:
				print("You lose! F")
				exit(1)
		print('you win! GG!')



if __name__ == '__main__':
	p = play()
	p.start()
