print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clotherspins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "Welcome to the Fantozzi Room."
    print "1. Shout to Ragionier Filini!"
    print "2. Play tennis with the Megadirettore."
    print "3. The Ragioniere is there! Wow!"

    fantozzi = raw_input("> ")

    if fantozzi == "1":
        print "Ragionier Filini brings you to an horrible corporate camping."
    elif fantozzi == "2":
        print "Che fa, batti? Batti Lei!"
    else:
        print "You instantly inherit Fantozzi's bad luck. Good luck!"

else:
    print "You stumple around on a knife and die. Good job!"
