#select whether you want to compare two methods by time and cost that gives you a minimum hourly profit

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
elif cost2 <= cost1:
    moreexpensive = method2

print(f"One person on your team would need to make at least ${hourlydiff}/hr within that saved time to justify the {moreexpensive}! Eg. if you take a more expensive method but save 2 hours, you must work in those 2 saved hours and make that necessary hourly wage if not more to justify the method. If you make more than this, then you will profit from the time savings (assuming you work with the time saved). If you make less than this, then this transportation is too expensive.")
