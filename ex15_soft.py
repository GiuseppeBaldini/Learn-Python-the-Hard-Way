print "Type here the name of the file:"

filename = raw_input('> ')

txt = open(filename)

print txt.read()
