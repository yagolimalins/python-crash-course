from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self, sides):
        random_number = randint(1, sides)
        return random_number

dice = Dice()

print("Six sided dice rolling ten times")
for rolling in range(0, 10):
    print(dice.roll_dice(6))

print("Ten sided dice rolling ten times")
for rolling in range(0, 10):
    print(dice.roll_dice(10))

print("Twenty sided dice rolling ten times")
for rolling in range(0, 10):
    print(dice.roll_dice(20))