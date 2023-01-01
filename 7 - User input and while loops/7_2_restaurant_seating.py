people = input("How many people are in your dinner group? ")
people = int(people)
if people > 8:
    print("You'll have to wait for a table")
elif people <= 8:
    print("Your table is ready")