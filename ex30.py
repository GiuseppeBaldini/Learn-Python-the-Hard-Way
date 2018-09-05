people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't dcide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

if cars / 2 > people:
    print "We should fit."
elif cars / 2 < people:
    print "We should check if we fit."
else:
    print "We should fit just right."

if trucks > cars and cars > people:
    print "Trucks. For sure."
elif cars > trucks and cars > people:
    print "Maybe we should take the cars."
else:
    print "Check the number of cars and trucks."
