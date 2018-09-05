def add(a, b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a,b)
    return a/b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d \nHeight: %d \nWeight:%d \nIQ: %d " %(age, height, weight, iq)


# A puzzle for extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, multiply(height, divide(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Here is my little equation."

ahii = multiply(iq, multiply(iq, (multiply(height, divide(age, 5)))))

print "And here we go: let me introduce you to %d." % ahii
