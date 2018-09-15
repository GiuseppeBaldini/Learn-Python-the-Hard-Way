splitstring = "I am a \nsplit string"
tall = 180
funny = "a really funny guy"
smart = "incredibly intelligent!"
combination = "Frank is %d cm tall, %r and ... \n\t%r" % (tall, funny, smart)

what = "A list"
how = "In a funny and weird way"
when = "In a timely manner"
weird_list = """
Building a weird list requires: \n\t* %s \n\t* %s \n\t* %s
""" % (what, how, when)

print splitstring
print combination
print weird_list
