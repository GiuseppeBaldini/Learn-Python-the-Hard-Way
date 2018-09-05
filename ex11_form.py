print "Insert your name here"
name = raw_input()
print "What are you doing with your life?"
job = raw_input()
print "For how many years have you walked this planet?"
age = raw_input()
print "Now serious staff: favourite food?"
food = raw_input()

print """Mmmm, you seem pretty cool, %s. Even if you are a %s years old %r and
I am just a poor 21 years old student, I am sure that we can find some
points in common. %s, for example!""" % (name, age, job, food)
