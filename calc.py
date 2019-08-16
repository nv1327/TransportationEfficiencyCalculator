options = input("Select options for your program: 1 - enter time and cost of two methods and receive a minimum hourly profit you must achieve, or enter time and cost and your hourly profit (and your team's) and it will tell you if it is too expensive: ")

if options == "1":
    import option1
elif options == "2":
    import option2

#a large step to add would be to use airline APIs to compare flights and get live flight times and prices and compare them to ferry APIs and private jet APIs
