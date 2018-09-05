def loop (days, days_skip):
    i = 0
    numbers = []
    while i < days:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + days_skip
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "

        for num in numbers:
            print num

print loop (10,2)
