class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The " + self.name.title() + " restaurant is specialized in " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        print(self.name.title() + " restaurant is open")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.ice_cream_flavours = ["chocolate", "strawberry"]

    def display_flavours(self):
        for flavour in icecreamstand.ice_cream_flavours:
            print(flavour)

icecreamstand = IceCreamStand("Gelato", "Ice Cream")

print(icecreamstand.name, icecreamstand.cuisine_type)
icecreamstand.display_flavours()