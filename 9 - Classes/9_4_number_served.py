class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The " + self.name.title() + " restaurant is specialized in " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        print(self.name.title() + " restaurant is open")

    def set_number_served(self):
        self.number_served = input("Set the number served: ")

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("giorno giovanna", "italian")

print(restaurant.name.title())
print(restaurant.cuisine_type + " food")

restaurant.open_restaurant()

restaurant.describe_restaurant()

print(restaurant.name.title() + " served " + str(restaurant.number_served) + " people")

restaurant.increment_number_served(10)

print(restaurant.name.title() + " restaurant served " + str(restaurant.number_served) + " people")