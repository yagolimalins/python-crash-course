person = {}

active = True

while active:
    name = input("What's your name? ")
    location = input("If you could visit one place in the world where would you go? ")
    person[name.lower()] = location.lower()
    pool_active = input("Do you want to continue the pool? (yes/no): ").lower()
    if pool_active == 'yes':
        continue
    elif pool_active == 'no':
        break

print(person)