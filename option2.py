#enter time and cost and your hourly profit (and your team's) and it will tell you if it is too expensive


name = input("Enter your name: ")
wage = input("Enter your estimated hourly profit/wage: ")
numbercheck = False
while numbercheck == False:
    try:
        float(wage)
    except ValueError:
        print ("This is not a number")
        wage = input("Please enter the estimated profit/wage again: ")
    else:
        numbercheck = True
team = {} #dictionary storing your team names and profits
team[name] = int(wage)
query = input("Would you like to add a team member?: ")
while query.lower() == "yes" or query.lower() == "yeah" or query.lower() == "true" or query.lower() == "yep" or query.lower() == "yup":
    name = input("Enter your team member's name: ")
    wage = input("Enter your team member's estimated hourly profit/wage: ")
    numbercheck = False
    while numbercheck == False:
        try:
            float(wage)
        except ValueError:
            print ("This is not a number")
            wage = input("Please enter the estimated profit/wage again: ")
        else:
            numbercheck = True
    team[name] = int(wage)
    query = input("Would you like to add another team member?: ")
else:
    query = "No"


teamwage = sum(team.values()) #this is the sum of all team members' wages

#print (team)
#print (sum(team.values()))

#First method of transportation
method1 = input("Enter your first tentative method of transportation (Eg. flight, ferry, bus ride): ")
time1 = input(f"Enter how long your {method1} takes in hours: ")
numbercheck = False
while numbercheck == False:
    try:
        float(time1)
    except ValueError:
        print ("This is not a number")
        time1 = input("Please enter the estimated time again: ")
    else:
        numbercheck = True


cost1 = input(f"Enter how much your {method1} costs: ")
numbercheck = False
while numbercheck == False:
    try:
        float(cost1)
    except ValueError:
        print ("This is not a number")
        cost1 = input("Please enter the estimated cost again: ")
    else:
        numbercheck = True

#Second mode of transportation
method2 = input("Enter your second tentative method of transportation (Eg. flight, ferry, bus ride): ")
time2 = input(f"Enter how long your {method2} takes in hours: ")
numbercheck = False
while numbercheck == False:
    try:
        float(time2)
    except ValueError:
        print ("This is not a number")
        time2 = input("Please enter the estimated time again: ")
    else:
        numbercheck = True

cost2 = input(f"Enter how much your {method2} costs: ")
numbercheck = False
while numbercheck == False:
    try:
        float(cost2)
    except ValueError:
        print ("This is not a number")
        cost2 = input("Please enter the estimated cost again: ")
    else:
        numbercheck = True


#Calculation
if cost1 >= cost2:
    moreexpensive = method1
elif cost2 >= cost1:
    moreexpensive = method2

timediff = abs(int(time1) - int(time2))
if timediff == 0:
    print(f"The {moreexpensive} is not worth it since both methods are the same amount of time.")
    exit()
costdiff = abs(int(cost1) - int(cost2))
hourlydiff = costdiff / timediff


if cost1 <= cost2:
    moreexpensive = method1
    lessexpensive = method2
elif cost2 <= cost1:
    moreexpensive = method2
    lessexpensive = method1

#if hourlydiff is greater than my hourly profits, then the moreexpensive is too expensive to justify!
if hourlydiff > teamwage:
    print(f"Your {moreexpensive} is too expensive! You would not be profiting by saving time on this, so take the {lessexpensive}.")
elif hourlydiff == teamwage:
    print(f"Both your {moreexpensive} and {lessexpensive} are viable options because they are both just as profitable in terms of comparing cost and time.")
else:
    print(f"Your {moreexpensive} is worth it because you will profit by saving time!")
