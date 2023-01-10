class Restaurant:
    """Creates a restaurant"""
    def __init__(self, name, cuisine_type):
        """Identifies the name and cuisine type of the restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe restaurant's name and cuisine type"""
        print("The " + self.name.title() + " restaurant is specialized in " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        """Opens the restaurant"""
        print(self.name.title() + " restaurant is open")
