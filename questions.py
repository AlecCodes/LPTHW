from random import randint
import fractions


def first_grade_question():
	while True:
		A = randint(1,10)
		B = randint(1,10)
		print('What is {} plus {}?'.format(A,B))
		guess = input("> ")
		try:
			if int(guess) == A+B:	
				return True
			else:
				return False
		except ValueError:
			print("\n Valid inputs only!\n")
			continue
		else:
			break


def second_grade_question():
	while True:
		try:	
			A = randint(0,10)
			B = randint(0,10)
			print("What is {} minus {}?".format(A,B))
			answer = int(input("> "))		
			if answer == A - B:
				return True 
			else:
				return False
		except ValueError:
			print("\n Valid inputs only!\n")
			continue
		else:
			break


def third_grade_question():
	while True:
		try:
			A = randint(0,100)
			B = randint(0,10)
			print("What is {} times {} ".format(A,B))
			answer = int(input("> "))			
			if answer == A * B:
				return True
			else:
				return False
		except ValueError:
			print("\n Valid inputs only!\n")
			continue
		else:
			break
			
	
def fourth_grade_question():
	while True:	
		try:
			deno = [2,4,8]
			A = deno[randint(0,2)]
			B = deno[randint(0,2)]
			print("What is 1/{} times 1/{}?".format(A,B))
			answer = input("> ")
			fraction_answer = fractions.Fraction(answer)	
			if fraction_answer == fractions.Fraction(1,A) * fractions.Fraction(1,B):
				return True
			else:
				return False 
		except ValueError:
			print("\nValid inputs only!\n")
			continue 
		else:
			break
		
		
def fifth_grade_question():
	while True:	
		try:
			A = randint(0,10)
			B = randint(0,4)
			C = randint(0,4)
			print ("What is {} to the power of {} times {} ".format(A,B,C))
			answer = int(input("> "))	
			if answer == (A**B) * C:
				return True
			else:
				return False
		except ValueError:
			print("\nValid inputs only!\n")
		else:
			break
