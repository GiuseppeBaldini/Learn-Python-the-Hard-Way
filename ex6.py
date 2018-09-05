# Defined x as a string
x = "There are %d types of people." % 10
# Defined binary as string "binary"
binary = "binary"
# Defined do_not as string "dont"
do_not = "don't"
# Define y as a string. We use both binary and do_not here
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x and then y
print x
print y

# Print "I said:" + x using format
print "I said: %r." % x
# Same thing with y
print "I also said: '%s'." % y

# Defined hilarious = False and joke_evaluation as a string
#with a NOT defined %r (weird!)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the variable that represent the string + hilarious (False)
print joke_evaluation % hilarious

# Define two new variables (w and e) with strings
w = "This is the left side of..."
e = "a string with a right side."

# Print these two new variables
print w + e
