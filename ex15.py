#Import argv
from sys import argv
#define argv with script and filename
script, filename = argv
#variable txt lets us open [filename]
txt = open(filename)
#print file named [filename]
print "Here's your file %r:" % filename
#read txt without further parameters
print txt.read()

txt.close()

print "Type the filename again:"
#insert new filename
file_again = raw_input("> ")
#open this new file
txt_again = open(file_again)
#print it
print txt_again.read()

txt_again.close()
