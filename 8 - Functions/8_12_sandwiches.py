def make_sandwich(*items):
    for item in items:
        print(item)

make_sandwich('salad', 'hamburger', 'bread')
make_sandwich('salad', 'hamburger')
make_sandwich('salad')