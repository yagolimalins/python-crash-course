sandwiches = ['farol', 'pajuçara', 'ponta verde', 'jatiuca', 'pinheiro']
finished_sandwiches = []

active = True

while sandwiches:
    current_sandwich = sandwiches.pop()
    print("I finished your " + current_sandwich.title() + " sandwich")
    finished_sandwiches.append(current_sandwich)

print()

while finished_sandwiches:
    print(finished_sandwiches.pop().title())