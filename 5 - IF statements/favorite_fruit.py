fruits = ['apple', 'watermelon', 'strawberry']

guess_fruit = input("Enter a fruit: ")

if guess_fruit.lower() in fruits:
    print("You guessed, I like " + guess_fruit.lower())
else:
    print("I don't like " + guess_fruit.lower())