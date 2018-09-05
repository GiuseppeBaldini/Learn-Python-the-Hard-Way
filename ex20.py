#import function argv
from sys import argv
#argv has 2 arguments: script and input_file
script, input_file = argv
#the function print_all takes f and read it
def print_all(f):
    print f.read()
#function rewind takes f and seek line n. 0 (beginning)
def rewind(f):
    f.seek(0)
#function print_a_line prints the first arg (line_count)
#and apply readline to f - then prints it
def print_a_line(line_count, f):
    print line_count, f.readline(),
#this variable opens input_file
current_file = open(input_file)
#call/run print_all
print "First let's print the whole file:\n"

print_all(current_file)
#call/run rewind
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
#applies the function print_a_line to current_line and current_file
current_line = 1
print_a_line(current_line, current_file)
#again
current_line += 1
print_a_line(current_line, current_file)
#aaaand again
current_line += 1
print_a_line(current_line, current_file)
