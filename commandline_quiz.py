from random import randint
from sys import exit
from commandline_flashcards import flashcards

#flashcards = {"1+1":'2', "2+2":'4', "3+3":'6'}
answers = list(flashcards.keys())
questions = list(flashcards.values())

def picker():
	global num
	num = randint(0,(len(answers)-1))
	print(questions[num])
	


def quizzer():

	while True:
		picker()
		answer = input(">")
		if answer == answers[num]:
			print('u win!')
			quit = input("play again? Y/N \n>")
			if quit == 'Y' or  quit == 'y':
				quizzer()
			if quit == 'N' or quit == 'n':
				exit(0) 
		else:
			print (answers[num])

quizzer()
