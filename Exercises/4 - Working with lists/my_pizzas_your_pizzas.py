pizzas = ['Bolonhesa', 'Portuguesa', 'Milanesa']

for pizza in pizzas:
    print("Eu gosto de pizza " + pizza)

print("Eu realmente amo pizza!")

friend_pizzas = pizzas[:]

pizzas.append('Don Leone')
friend_pizzas.append('Calabresa')

for pizza in pizzas:
    print("My favorite pizzas are: " + pizza)

for pizza in friend_pizzas:
    print("My favorite pizzas are: " + pizza)