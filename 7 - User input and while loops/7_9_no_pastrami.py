sandwich_orders = ['farol', 'pastrami', 'pajuçara', 'ponta verde', 'pastrami', 'jatiuca', 'pinheiro', 'pastrami']

print('The deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print()

while sandwich_orders:
    print(sandwich_orders.pop())