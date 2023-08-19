from sys import argv

script, input_file = argv
#read and print
def print_all(f):
	print(f.read())
#
def rewind(f):
	f.seek(0)
#each time readline is called on f, it goes to the next line of the text
def print_a_line(line_count,f):
	print(line_count, f.readline())
#opens file we pass as argument for ex20
current_file = open(input_file)	
#prints without using print_a_line
print("first lest print the whole file: \n")

print_all(current_file)

print("Now lest rewind, kind of like a tape")
#readline resets the offset(think of it like a blinking cursor) to 0, so readline can be called again to cycle thru lines
rewind(current_file)

print("Lets print three lines")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
