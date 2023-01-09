class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        self.battery_size = 85

class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_car = EletricCar("Tesla", "Model S", "2016")

my_car.battery.get_range()

my_car.battery.upgrade_battery()

my_car.battery.get_range()