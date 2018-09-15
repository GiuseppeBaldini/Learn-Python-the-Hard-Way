from sys import argv

script, user_name, language = argv
prompt = 'Insert answer: '

print """
Hi %s, I'm the %s script and I am written in %s.
""" % (user_name, script, language)

print "I'd like to ask you a few questions."

print "How would you define the experience of learning %s?" %language
opinion = raw_input(prompt)

print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You said you have a %r computer and learning %r is %r.
Thank you for this.
""" % (likes, lives, computer, language, opinion)
