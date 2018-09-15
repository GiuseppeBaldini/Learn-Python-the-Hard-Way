from sys import argv

script, user, activity = argv

prompt = 'What about answering here? '

print """ Ok %s, here are a couple of questions for you.
Oh, nice to meet you, I am %s.
Hope you are enjoying %s so far """ % (user, script, activity)

print "So, what's your full name?"
name = raw_input(prompt)

print "And I forgot where you live. Where is it again?"
location = raw_input(prompt)

print """Ok, if I recall correctly you
are %s and live in %s. Good.""" % (name, location)

print "Is it correct?"
answer = raw_input("Yes or no? ")

if answer == "Yes":
    print "Yes! I knew it!"
else:
    print "Ok, my memory is very bad. What's your name again?"
    name_again = raw_input("Yes, type it here: >> ")
if name == name_again:
    print "Oh, I remember you now. Cool guy!"
else:
    print "But you said your name was \"%s\"!" % name
