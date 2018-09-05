cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#Since we have 1 driver per car, we can find cars not driven
#with a simple subtraction
cars_not_driven = cars - drivers
#Here is the assumption stated before. 1 car = 1 driver
cars_driven = drivers
#Our total capacity is given by the number of cars multiplied
#by the number of people that each car can contain
carpool_capacity = cars_driven * space_in_a_car
#Here we calculate the average passenger that we need to accomodate
#in each car in order to allocate all our carpooling capacity
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity,"people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."
