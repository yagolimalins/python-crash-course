toppings = []
active = True

while active:
    topping = input("Enter a topping for your pizza: ")
    if topping == 'quit':
        active = False
    else:
        toppings.append(topping)
        for topping in toppings:
            print(topping)