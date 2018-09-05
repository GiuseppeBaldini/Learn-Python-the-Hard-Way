def loop(days, days_skip):
    i = 0
    numbers = []
    for i in range (0, days):
        print "At the top is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

        for num in numbers:
            print num

print loop (10, 2)
