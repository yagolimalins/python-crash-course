ordinal_numbers = [x + 1 for x in range(0,9)]
print(ordinal_numbers)

for number in ordinal_numbers:
    if int(number) == 1:
        print("1st")
    elif int(number) == 2:
        print('2nd')
    elif int(number) == 3:
        print("3rd")
    elif int(number) >= 4 and int(number) < 10:
        print(str(number) + "th")
    elif number not in range(0,9):
        print("number out of range")