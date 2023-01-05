def make_car(brand, model, **kwargs):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in kwargs.items():
        car[key] = value
    return car

car = make_car('fiat', 'uno', color='blue', year='2008')

print(car)