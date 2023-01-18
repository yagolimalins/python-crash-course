first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
    result = int(first_number) + int(second_number)
except ValueError:
    print("One or both values entered are not a decimal")
else:
    print(result)