class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("The " + self.name.title() + " restaurant is specialized in " + self.cuisine_type + " cuisine")
    
    def open_restaurant(self):
        print(self.name.title() + " restaurant is open")
    
restaurant = Restaurant("giorno giovanna", "italian")

print(restaurant.name.title())
print(restaurant.cuisine_type + " food")

restaurant.open_restaurant()

restaurant.describe_restaurant()