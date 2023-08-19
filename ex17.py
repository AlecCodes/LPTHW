from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#indata = open(from_file).read()

#print(f"the input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN To continue, CTRL-C to abort.")
#input()
#ALL ON ONE LINE!
open(to_file,'w').write(open(from_file).read())

print("Alright all done")

#to_file.close()
#from_file.close()

trye = """AB
C"""
print(len(trye))
