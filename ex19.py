#define the function "cheese_and_crackers" as a combination
#of 4 prints - with argument cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#print sentence and give directly numerical values to the args
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#alternative: we are using variables as arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#we define that cheese_count = amount_of_cheese and
#boxes_of_crackers = amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#show how you can math operations as arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#combine variables and math operations as new arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)
