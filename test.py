class Fighter:
    def __init__(self, name, life = 100, atk = 100):
        self.name = name
        self.life = life
        self.atk = atk
        self.defending = False

    def attack(self, foe):
        if not foe.defending:
            print(self.name + " attacked")
            foe.life -= self.atk
            print(foe.name + " life has been reduced to " + str(foe.life))

yago = Fighter("Yago", atk=10)
edgar = Fighter("Edgar")

while True:
    command = input()
    if command == 'a':
        yago.attack(edgar)
    command = "x"
    if edgar.life == 0:
        print("\nGAME OVER")
        break