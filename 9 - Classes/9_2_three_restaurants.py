class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("The " + self.name.title() + " restaurant is specialized in " + self.cuisine_type + " cuisine")
    
    def open_restaurant(self):
        print(self.name.title() + " restaurant is open")
        
restaurant_1 = Restaurant("giorno giovanna", "italian")
restaurant_2 = Restaurant("bruno bucciarati", "italian")
restaurant_3 = Restaurant("guido mista", "italian")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()