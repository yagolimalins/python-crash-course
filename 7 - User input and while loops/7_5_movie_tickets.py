while True:
    age = int(input("Enter your age: "))
    if age < 3:
        price = 0
    elif (age >= 3) and (age <= 12):
        price = 10
    elif age > 12:
        price = 15
    print("The ticket costs: $" + str(price))