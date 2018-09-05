# our initial list (supposed to be of 10 items, but..)
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#.. but it is not. And we print this clever observation
print "Wait there are not 10 things in that list. Let's fix that."
# splitting the initial list every time we encounter ' ' aka a space
stuff = ten_things.split(' ')
# here is the list we will use to fill the initial one
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# until stuff has less then 10 elements
while len(stuff) != 10:
    # call pop with argument more_stuff
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    # call append on next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!
