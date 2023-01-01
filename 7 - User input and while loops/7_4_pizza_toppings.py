toppings = []

while True:
    topping = input("Enter a topping for your pizza: ")
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        for topping in toppings:
            print(topping)