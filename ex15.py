#import argv package so that we can accept args in cmd line
from sys import argv
#unpack args, script is ex15.py, since thats technically the first argument
script, filename = argv
#this makes a variable 'txt', and stores within it the value returned from calling open on 'filename'
txt = open(filename)
#prints out the name of our file, then .read is called on txt to print out the contents of the file
print(f"here is your file {filename}")
print(txt.read())
txt.close()
#asks user for the name of file, and saves that to file_agin by using the input function
print("Type the filename again:")
file_again = input("> ")
#passing file_again into the open function yields the same result as passing filetime into the open function
txt_again = open(file_again)
#therefore we can call read to print the contents of the same file
print(txt_again.read())
txt_again.close()
