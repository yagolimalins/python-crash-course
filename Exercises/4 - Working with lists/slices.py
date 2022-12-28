numbers = []
for number in range(1,1000000+1):
    numbers.append(number)

print("The first three items in the list are: " + str(numbers[:3]))

print("Three items from the middle of the list are: " + str(numbers[499998:500001]))

print("The last three items in the list are: " + str(numbers[-3:]))