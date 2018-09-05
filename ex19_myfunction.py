def monthly_budget(rent, food, extra):
    print "Let's see how much I am going to spend this month."
    print "I have rent expenses for %d" % rent
    print "Food is relatively cheaper, costing %d per month." % food
    print "Extra expenses accounted for %d." % extra
    total = rent + food + extra
    print "Ok, it seems that this month I will spend %d." % total

monthly_budget (400, 280, 100)

hostel_per_week = 90
hostel_per_month = hostel_per_week * 4
food_expenses = 250

going_out = 100
purchases = 10
extra_expenses = going_out + purchases

monthly_budget (hostel_per_month, food_expenses, extra_expenses)

rent_input = int(raw_input())
food_input = int(raw_input())
extra_input = int(raw_input())

monthly_budget (rent_input, food_input, extra_input)
