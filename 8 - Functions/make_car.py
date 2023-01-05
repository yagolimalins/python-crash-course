def make_car(brand, model, **kwargs):
    """Makes a car"""
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in kwargs.items():
        car[key] = value
    return car